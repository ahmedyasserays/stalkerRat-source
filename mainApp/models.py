from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from gdstorage.storage import GoogleDriveStorage

# Create your models here.

# Define Google Drive Storage
gd_storage  =  GoogleDriveStorage ()

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Profile")
    profilePic = models.ImageField(null=True, blank=True, default='profilePics/colorfull_user.png', upload_to='profilePics/', storage=gd_storage)

    def __str__(self):
        return self.user.get_full_name()

    def messages(self):
        result = []
        for message in self.message_set.all():
            result.append(message.content)
        return mark_safe(f'<a href="https://stalker-rat.herokuapp.com/view_messages/{self.id}">show {self.message_set.count()} messages</a>')


class message(models.Model):
    content = models.TextField()
    sent_to = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
