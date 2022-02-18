from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import SignUpForm


class SubmittableLoginView(LoginView):
    template_name = "forms/form.html"


class SubmittablePasswordChangeView(PasswordChangeView):
    template_name = 'forms/form.html'
    success_url = reverse_lazy('index')


class SignUpView(CreateView):
    template_name = 'forms/form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')
