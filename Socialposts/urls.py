from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('posts/create', views.post_create_view, name='post-create'),
    path('posts/delete/<pk>/', views.post_delete_view, name='post-delete'),
    path('posts/edit/<pk>/', views.post_edit_view, name='post-edit'),
    path('posts/<pk>/', views.post_page_view, name='post'),
    path('post/<pk>/like/', views.like_post, name="like-post"),
    path('comment/like/<pk>/', views.like_comment, name="like-comment"),
    path('reply/like/<pk>/', views.like_reply, name="like-reply"),
    path('commentsent/<pk>/', views.comment_sent, name='comment-sent'),
    path('comment/delete/<pk>/', views.comment_delete_view, name='comment-delete'),
    path('reply-sent/<pk>/', views.reply_sent, name='reply-sent'),
    path('reply/delete/<pk>/', views.reply_delete_view, name='reply-delete'),
]
