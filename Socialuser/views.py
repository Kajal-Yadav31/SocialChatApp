from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Profile
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse
# Create your views here.


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('profile-registercreate')
            else:
                return HttpResponse('Invalid credentials')

    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            try:
                new_user = user_form.save(commit=False)
                new_user.set_password(user_form.cleaned_data['password'])
                new_user.save()
                messages.success(request, 'Registeration Done!')
                Profile.objects.create(user=new_user)

            except IntegrityError:
                pass
            # return redirect('home')
            # login(request, new_user)

            # return render(request, 'user/register_done.html')
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        messages.error(request, 'Some is wrong')
    return render(request, 'user/register.html', {'user_form': user_form})


@login_required
def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            raise Http404()
    return render(request, 'user/profile.html', {'profile': profile})


@login_required
def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,
                           instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')

    if request.path == reverse('profile-registercreate'):
        template = 'user/profile_registercreate.html'
    else:
        template = 'user/profile_edit.html'

    return render(request, template, {'form': form})


@login_required
def profile_delete_view(request):
    user = request.user

    if request.method == 'POST':
        logout(request)
        user.delete()
        messages.success(request, 'Account deleted')
        return redirect('home')
    return render(request, 'user/profile_delete.html')
