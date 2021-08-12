from django.shortcuts import render, redirect
from django.contrib import messages
from django.forms.models import inlineformset_factory
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files import File
from .forms import SignUpForm, UpdateUserForm
from .models import userProfile, message
from .decorators import restrict_logged, restrict_unlogged, admin_only
from tempfile import NamedTemporaryFile
from os.path import basename
from PIL import Image
from webpush import send_user_notification
import io, requests

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        url = request.build_absolute_uri(f'/user/{request.user.id}')
        user_messages = request.user.Profile.message_set.all().order_by('-date_sent')
        webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
        vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
        context = {
            'userLink':url,
            'user_messages':user_messages,
            'vapid_key': vapid_key,
        }
        return render(request, 'home5.html', context)
    else:
        context = {
            "users_counter": User.objects.count()
        }
        return render(request, 'home2.html', context=context)

@restrict_logged
def signUp(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            userProfile.objects.create(user=user)
            username = form.cleaned_data.get("username")
            messages.success(request, f"Your account was created successfully, {username}")
            return redirect('login')
    context = {'form': form}
    return render(request, 'signUp2.html', context)

@restrict_logged
def loginUser(request):
    context = {}
    if request.method == "POST":
        user_name = request.POST.get("your_name")
        user_pass = request.POST.get("your_pass")
        user = authenticate(request, username=user_name, password=user_pass)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "The username or password you entered is not correct")
    return render(request, 'login2.html', context)  

@restrict_unlogged
def logoutuser(request):
    logout(request)
    return redirect("home")

def search(request):
    if request.method == 'POST':
        search_word = request.POST['search_word'].strip()
        if search_word:        
            if ' ' in search_word:
                search_words = search_word.split(' ')
                print(search_words)
                users = User.objects.none()
                for word in search_words:
                    users = users | User.objects.filter(Q(first_name__contains=word) | Q(last_name__contains=word) | Q(username__contains=word))
            else:
                users = User.objects.filter(Q(first_name__contains=search_word) | Q(last_name__contains=search_word) | Q(username__contains=search_word))
        else:
            users = User.objects.none()
        context = {"search_word":search_word, "users":users}
        return render(request, 'search2.html', context)
    return render(request, 'search2.html')

def viewUser(request, userId):
    target_user =  User.objects.get(id=userId).Profile
    if request.user.is_authenticated:
        if target_user == request.user.Profile:
            return redirect('home')
    message_form_set = inlineformset_factory(userProfile, message, fields=('content',), extra=1)
    message_form = message_form_set(queryset=message.objects.none() , instance=target_user)
    if request.method == "POST":
        message_form = message_form_set(request.POST, instance=target_user)
        if message_form.is_valid():
            result_message = message_form.save()
            message_content:str = result_message[0].content
            if len(message_content) > 100 :
                message_content = message_content[:message_content.find(" ", 85)]
            payload = {
                "head":"Some one sent You a new message",
                "body":message_content
            }
            send_user_notification(
                user=target_user.user,
                payload=payload,
                ttl=1000,
            )
            if request.user.is_authenticated:
                result_message[0].sender = request.user
                result_message[0].save()
            messages.success(request, "message was sent successfully")
            context = {"user":target_user, 'formset': message_form}
            return redirect('user', userId=userId)
    context = {
        "user":target_user,
        "formset": message_form,
    }
    return render(request, 'viewUser.html', context)

@restrict_unlogged
def updateProfile(request):
    user = request.user
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=user)
        isUserFormValid = user_form.is_valid()
        if isUserFormValid:
            user_form.save()
        image_url = request.POST['hidden_image']
        if image_url:
            img_temp = NamedTemporaryFile(delete=True)
            image_content = requests.get(image_url).content
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file).convert('RGB')
            image.save(img_temp, "JPEG", quality=50)
            img_temp.flush()

            user.Profile.profilePic.save(basename(image_url), File(img_temp))
            user.Profile.save()

        if isUserFormValid:
            return redirect('home')
        
        context = { 'user_form': user_form}
        return render(request, 'newUpdateProfile.html', context)


    user_form = UpdateUserForm(instance=user)
    context = { 'user_form': user_form}
    return render(request, 'newUpdateProfile.html', context)

@restrict_unlogged
def removePic(request):
    request.user.Profile.profilePic = userProfile._meta.get_field("profilePic").get_default()
    request.user.Profile.save()
    return redirect('updateProfile')

@admin_only
def admin_messages(request, id):
    target = userProfile.objects.get(id=id)
    all_messages = target.message_set.all()
  
    return render(request, 'adminViewMessage.html', {"userMessags":all_messages})
