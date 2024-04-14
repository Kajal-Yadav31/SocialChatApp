from django.shortcuts import render
from accounts.models import Account
from inbox.models import ChatModel
# Create your views here.


def index(request):
    users = Account.objects.exclude(username=request.user.username)
    return render(request, 'inbox/index.html', context={'users': users})


def chatpage(request, username):
    user_obj = Account.objects.get(username=username)
    users = Account.objects.exclude(username=request.user.username)

    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'

    message_obj = ChatModel.objects.filter(thread_name=thread_name)

    return render(request, 'inbox/main_chat.html', context={'users': users, 'user': user_obj, 'messages': message_obj})
