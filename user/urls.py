"""user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from django.utils.functional import new_method_proxy
from accounts.views import (
    index,
    signin_view,
    user_view,
    logout_view,
    profile_view,
    signup_view,
    auth_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index, name='home'),
    path('home/login/', signin_view, name='signin'),
    path('account/', user_view, name='user'),
    path('signout/', logout_view, name='signout'),
    path('account/profile/', profile_view),
    path('home/signup/', signup_view, name='signup'),
    path('home/authentication/', auth_view, name='auth'),
    path('', views.LoginView.as_view(
        redirect_authenticated_user=True), name='login')
]
