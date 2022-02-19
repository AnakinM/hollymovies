from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import SubmittableLoginView, SignUpView, SubmittablePasswordChangeView

app_name = 'accounts'
urlpatterns = [
    path('login/', SubmittableLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('password-change/', SubmittablePasswordChangeView.as_view(), name='password_change'),
]
