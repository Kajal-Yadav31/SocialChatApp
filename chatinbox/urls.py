from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox_view, name='inbox_view'),
    path('c/<conversation_id>/', views.inbox_view, name='inbox_view'),
    # path('search_users/', views.search_users, name='inbox_searchusers'),
    # path('new_message/<recipient_id>',
    #      views.new_message, name='inbox_newmessage'),
    # path('new_reply/<conversation_id>/', views.new_reply, name="inbox-newreply"),
    #     path('notify/<conversation_id>/', notify_newmessage, name="notify-newmessage"),
    #     path('notify-inbox/', notify_inbox, name="notify-inbox"),
]
