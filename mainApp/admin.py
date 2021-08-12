from django.contrib import admin
from django.urls import path
from .models import message, userProfile


# Register your models here.

# @admin.register(message, site=admin_site)
class messagesAdmin(admin.ModelAdmin):
    list_display = ('content', 'sent_to', 'sender')
    
class userProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'messages')

admin.site.register(message, messagesAdmin)
admin.site.register(userProfile, userProfileAdmin)
