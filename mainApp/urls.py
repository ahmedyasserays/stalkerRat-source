from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *



urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
    path('signup/', signUp, name='signUp'),
    path('login/', loginUser, name='login'), 
    path('logout/', logoutuser, name='logout'),
    path('user/<int:userId>/', viewUser, name="user"),
    path('updateProfile/', updateProfile, name='updateProfile'),
    path('removePic', removePic, name='removePic'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='resetPassword.html'), name='password_reset'),
    path('reset_email_sent/', auth_views.PasswordResetDoneView.as_view(template_name='emailSent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='newPassword.html'), name='password_reset_confirm'),
    path('password_reset_successfully/', auth_views.PasswordResetCompleteView.as_view(template_name='passwordResetDone.html'), name='password_reset_complete'),
    path('view_messages/<int:id>/', admin_messages, name='admin_messages'),
]
