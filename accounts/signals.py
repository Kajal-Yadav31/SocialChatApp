from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile, Account
from django.shortcuts import get_object_or_404


@receiver(post_save, sender=Account)
def create_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        Profile.objects.create(
            user=user,
        )
    else:
        profile = get_object_or_404(Profile, user=user)
        profile.save()


@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    profile = instance
    if created == False:
        user = get_object_or_404(Account, id=profile.user.id)
        if user.email != profile.user.email:
            user.email = profile.user.email
            user.save()
