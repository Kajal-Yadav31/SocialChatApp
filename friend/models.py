# from django.db import models
# from django.conf import settings
# from django.utils import timezone
# from accounts.models import Account

# # Create your models here.


# class FriendList(models.Model):
#     user = models.OneToOneField(
#         Account, on_delete=models.CASCADE, related_name="user")
#     friends = models.ManyToManyField(
#         Account, blank=True, related_name="friends")

#     def __str__(self):
#         return self.user.username

#     def add_friend(self, account):
#         if not account in self.friends.all():
#             self.friends.add(account)

#     def remove_friend(self, account):
#         if account in self.friends.all():
#             self.friends.remove(account)

# # Initiate the action of unfriending someone
#     def unfriend(self, removee):
#         # the removee-> is the person you want to unfriend from the friend list
#         remover_friend_list = self  # person terminating the friendship

#         # Remove friend from remover friend list
#         remover_friend_list.remove_friend(removee)

#         # Remove friend from removee friend list
#         friends_list = FriendList.objects.get(user=removee)
#         friends_list.remove_friend(self.user)

#     def is_mutual_friend(self, friend):
#         # chacking Is this a friend?
#         if friend in self.friends.all():
#             return True
#         return False


# class FriendRequest(models.Model):
#     """
#         A friend request consist of two main parts:
#             1. SENDER:
#                 - Person sending the friend request
#             2. RECEIVER:
#                 - Person receiving the friend request
#     """
#     sender = models.ForeignKey(
#         Account, on_delete=models.CASCADE, related_name="sender")
#     receiver = models.ForeignKey(
#         Account, on_delete=models.CASCADE, related_name="receiver")
#     is_active = models.BooleanField(blank=True, null=False, default=True)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.sender.username
