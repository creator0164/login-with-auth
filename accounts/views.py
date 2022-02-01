from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.views.generic.base import RedirectView


def session_view(request):
    request.session.set_expiry(10)


def index(request, *args, **kwargs):
    return render(request, 'index.html')


def signin_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('user')
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                username_ = user.username
                request.session['user'] = username_
                return redirect('user')
            elif not request.user.is_authenticated:
                messages.error(request, 'You are not authenticated.')
            else:
                messages.error(request, 'Username and password are not match.')
    except:
        redirect('signin')

    return render(request, 'login.html')


@login_required(login_url='/home/login/')
def user_view(request, *args, **kwargs):

    return render(request, 'user.html')


@login_required(login_url='/home/login/')
def profile_view(request, *args, **kwargs):
    return render(request, 'profiles_.html')


def logout_view(request, *args, **kwargs):
    logout(request)
    messages.success(request, 'Logged out success')
    return redirect('signin')


def signup_view(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(username=username):
            messages.error(request, 'Username is already exist')
            return redirect('signup')
        elif User.objects.filter(email=email):
            messages.error(request, 'Email is already exist')
            return redirect('signup')
        elif password != confirm_password:
            messages.error(request, 'Password are not match.')
            return redirect('signup')
        elif len(username) > 10:
            messages.error(request, 'Username must be under 10 characters.')
            return redirect('signup')
        elif not username.isalnum:
            messages.error(request, 'Username must be Alpha numeric')
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            user.is_active = False
            user.save()
            return redirect('auth')
    return render(request, 'signup.html')


def auth_view(request, *args, **kwargs):
    return render(request, 'authentication.html')
