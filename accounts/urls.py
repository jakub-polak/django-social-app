from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from django.urls import path, reverse_lazy

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path(
        '',
        views.home,
        name='home',
    ),
    path(
        'login/',
        LoginView.as_view(template_name='accounts/login.html'),
        name='login',
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='accounts/logout.html'),
        name='logout',
    ),
    path(
        'register/',
        views.register,
        name='register',
    ),
    path(
        'profile/',
        views.view_profile,
        name='view_profile',
    ),
    path(
        'profile/edit',
        views.edit_profile,
        name='edit_profile',
    ),
    path(
        'change-password/',
        views.change_password,
        name='change_password',
    ),
    path(
        'reset-password/',
        PasswordResetView.as_view(
            template_name='accounts/password_reset.html',
            email_template_name='accounts/password_reset_email.html',
            success_url=reverse_lazy('accounts:password_reset_done'),
        ),
        name='password_reset',
    ),
    path(
        'reset-password/done/',
        PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    path(
        'reset-password/confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_confirm.html',
            success_url=reverse_lazy('accounts:password_reset_complete'),
        ),
        name='password_reset_confirm',
    ),
    path(
        'reset-password/complete/',
        PasswordResetCompleteView.as_view(
            template_name='accounts/password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
]
