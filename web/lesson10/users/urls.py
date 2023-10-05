from django.contrib.auth.views import PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
from django.urls import path

from . import views as v


app_name = 'users'

urlpatterns = [
    path('signup/', v.signupuser, name='signup'),
    path('login/', v.loginuser, name='login'),
    path('logout/', v.logoutuser, name='logout'),
    path('reset-password/', v.ResetPasswordView.as_view(), name='password_reset'),
    path(
        'reset-password/done/',
        PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'reset-password/confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html',
            success_url='/users/reset-password/complete/'
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset-password/complete/',
        PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'
    ),
]
