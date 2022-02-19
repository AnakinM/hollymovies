from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import SubmittableLoginView, SignUpView, SubmittablePasswordChangeView, ProfileUpdateView, ProfileDetailsView

app_name = 'accounts'
urlpatterns = [
    path('login/', SubmittableLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('password-change/', SubmittablePasswordChangeView.as_view(), name='password_change'),
    path('profile/<int:pk>/', ProfileDetailsView.as_view(), name='profile'),
    path('profile/<int:pk>/update/', ProfileUpdateView.as_view(), name='update_profile'),
]
