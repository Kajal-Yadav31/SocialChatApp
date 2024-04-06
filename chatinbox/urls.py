from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.chat_page, name="inbox_view"),
]
