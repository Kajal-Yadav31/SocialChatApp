from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('<str:username>/', views.chatpage, name='chat'),
]
