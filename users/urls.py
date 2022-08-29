from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import path

from users.views import SignUp, ProfileUpdate, ProfileCreate

app_name='users'

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', LoginView.as_view(
        template_name='users/login.html'), name='login'),
    path('profilecreate/', login_required(ProfileCreate.as_view()), name='profile_create'),
    path('profileupdate/', login_required(ProfileUpdate.as_view()), name='profile_update'),
]
