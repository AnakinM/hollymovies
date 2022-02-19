from django.contrib import admin
from django.urls import path

from viewer.views import SubmittableLoginView
from viewer.models import Genre, Movie

admin.site.register(Genre)
admin.site.register(Movie)

urlpatterns = [
    path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
]
