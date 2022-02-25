from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from accounts.forms import UserCreationForm, SignUpForm, UserProfileUpdateForm, UserAccountUpdateForm
from accounts.models import Profile


class SubmittableLoginView(LoginView):
    template_name = "forms/form.html"


class SignUpView(CreateView):
    template_name = "forms/form.html"
    form_class = SignUpForm
    success_url = reverse_lazy('index')


class SubmittablePasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "forms/form.html"
    success_url = reverse_lazy('index')


class ProfileUpdateView(UpdateView):
    template_name = "forms/form.html"
    form_class = UserProfileUpdateForm
    model = Profile
    success_url = reverse_lazy('index')


class AccountUpdateView(UpdateView):
    template_name = "forms/form.html"
    form_class = UserAccountUpdateForm
    model = User
    success_url = reverse_lazy('index')


class ProfileDetailsView(DetailView):
    template_name = "profile.html"
    model = Profile
