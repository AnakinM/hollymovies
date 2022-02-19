"""hollymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from viewer.views import search, MoviesView, MovieCreateView, ContactView, GreetingView, GenreCreateView, \
    MovieUpdateView, MovieDeleteView, MovieDetailView, GenreListView, GenreUpdateView, SubmittableLoginView
from viewer.models import Genre, Movie

admin.site.register(Genre)
admin.site.register(Movie)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', SubmittableLoginView.as_view(), name='login'),
    path('search/', search, name="search"),
    path('movies/', MoviesView.as_view(), name="movies"),
    path('movies/new', MovieCreateView.as_view(), name="create_movie"),
    path('movies/<int:pk>', MovieDetailView.as_view(), name="read_movie"),
    path('movies/<int:pk>/update', MovieUpdateView.as_view(), name="update_movie"),
    path('movies/<int:pk>/delete', MovieDeleteView.as_view(), name="delete_movie"),
    path('genres/', GenreListView.as_view(), name="genres"),
    path('genres/new', GenreCreateView.as_view(), name="create_genre"),
    path('genres/<int:pk>/update', GenreUpdateView.as_view(), name="update_genre"),
    path('contact/', ContactView.as_view(), name='contact'),
    path('greeting/', GreetingView.as_view(greeting="Hello"), name='greeting'),
    path('', TemplateView.as_view(template_name="home.html"), name='index'),
]
