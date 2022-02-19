from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import UserCreationForm


class SubmittableLoginView(LoginView):
    template_name = "forms/form.html"


class SignUpView(CreateView):
    template_name = "forms/form.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('index')


class SubmittablePasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "forms/form.html"
    success_url = reverse_lazy('index')
