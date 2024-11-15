from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterationForm
from .models import Account, Profile
from Socialposts.models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import *
from django.db.models import Q

# verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from .tasks import email_send_task

# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegisterationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()

            # user activation
            domain = get_current_site(request)
            email_send_task.delay(
                user.id, email, get_current_site(request).domain)

            return redirect('/accounts/login/?command=verification&email='+email)

    else:
        form = RegisterationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        users = authenticate(email=email, password=password)
        print('user:', users)

        if users is not None:
            login(request, users)
            return redirect('profile-registercreate')

        else:
            messages.error(request, 'Please! Enter correct email and password')
            return redirect('login')
    return render(request, 'accounts/login_user.html')


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')


def activate(request, uidb64, token):
    return HttpResponse('Ok')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(
            request, 'Congratulations! Your account is activated.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')


def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            # user activation
            current_site = get_current_site(request)
            mail_subject = 'Reset your Password'
            message = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(
                request, 'Password reset email has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist!')
            return redirect('forgotPassword')
    return render(request, 'accounts/forgotPassword.html')


def reset_password_validate(request,  uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please reset your password')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('login')


def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('resetPassword')
    else:
        return render(request, 'accounts/resetPassword.html')


@login_required
def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(Account, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            raise Http404()

    return render(request, 'accounts/profile.html', {'profile': profile})


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
        template = 'accounts/profile_registercreate.html'
    else:
        template = 'accounts/profile_edit.html'

    return render(request, template, {'form': form})


@login_required
def profile_delete_view(request):
    user = request.user

    if request.method == 'POST':
        logout(request)
        user.delete()
        messages.success(request, 'Account deleted')
        return redirect('home')
    return render(request, 'accounts/profile_delete.html')


def account_search_view(request):
    query = request.GET.get('q', '')
    users = []

    if query:
        users = Account.objects.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        ).exclude(id=request.user.id)

    context = {
        'accounts': users,
    }

    return render(request, 'accounts/search_user.html', context)
