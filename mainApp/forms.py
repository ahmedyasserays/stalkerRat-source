from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {
                "id":"usernameone",
                "placeholder":"First name",
                "autocomplete":"given-name"
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                "id":"usernamelast",
                "placeholder":"Last name",
                "autocomplete":"family-name"
            }
        )
        self.fields['username'].widget.attrs.update(
            {
                "id":"username",
                "placeholder":"Username",
                "autocomplete":"off"
                
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                "id":"email",
                "placeholder":"Email address",
                "autocomplete":"email"
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                "id":"password",
                "placeholder":"Password",
                "autocomplete":"new-password"
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                "id":"repeat-password",
                "placeholder":"Repeat password",
                "autocomplete":"new-password"
            }
        )

class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
    
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {
                'id':'editNameone'
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'id':'editNamelast'
            }
        )
        self.fields['username'].widget.attrs.update(
            {
                'id':'editUserName'
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'id':'editEmail'
            }
        )
