from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('password_change/', auth_view.PasswordChangeView.as_view(
        template_name='user/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_view.PasswordChangeDoneView.as_view(
        template_name='user/password_change_done.html'), name='password_changedone'),
    path('password_reset/', auth_view.PasswordResetView.as_view(
        template_name='user/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(
        template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_view.PasswordResetConfirmView.as_view(
        template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_view.PasswordResetConfirmView.as_view(
        template_name='user/password_reset_complete.html'), name='password_reset_complete'),

    #
    path('profile/', views.profile_view, name='profile'),
    path('<username>/', views.profile_view, name='userprofile'),
    path('profile/edit', views.profile_edit_view, name='profile-edit'),
    path('profile/delete', views.profile_delete_view, name='profile-delete'),
    path('profile/registercreate/', views.profile_edit_view,
         name='profile-registercreate'),
]
