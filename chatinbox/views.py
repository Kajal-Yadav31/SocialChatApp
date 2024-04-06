from django.shortcuts import render


def chat_page(request):
    return render(request, 'chatinbox/inbox.html')
