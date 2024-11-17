# tasks.py
from SocialMedia.celery import app
from celery import shared_task
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from accounts.models import Account


@shared_task(bind=True)
def email_send_task(self, user_id, email, domain):
    print("Task started")
    try:
        user = Account.objects.get(id=user_id)
        mail_subject = 'Please activate your account'
        message = render_to_string('accounts/account_verification_email.html', {
            'user': user,
            'domain': domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        send_email = EmailMessage(mail_subject, message, to=[email])
        result = send_email.send()
        if result == 1:
            print("Email sent successfully")
        else:
            print("Failed to send email")
    except Exception as e:
        print(f"Failed to send email: {e}")

    return 'Task executed successfully'


@shared_task(bind=True)
def ForgotPassword_send_task(self, user_id, email, domain):
    print("Forgot Password Task started")
    try:
        user = Account.objects.get(id=user_id)
        mail_subject = 'Please Reset your Password'
        message = render_to_string('accounts/reset_password_email.html', {
            'user': user,
            'domain': domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        send_email = EmailMessage(mail_subject, message, to=[email])
        result = send_email.send()
        if result == 1:
            print("Forgot Password Email sent successfully")
        else:
            print("Forgot Password Failed to send email")
    except Exception as e:
        print(f"Forgot Password Failed to send email: {e}")

    return 'Forgot Password Task executed successfully'
