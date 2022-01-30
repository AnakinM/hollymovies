from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView, TemplateView

from viewer.forms import MovieForm, GenreForm
from viewer.models import Movie, Genre


def search(request):
    title = request.GET.get("title")
    if title:
        data = Movie.objects.filter(title__contains=title)
        return render(request, "search.html", context={'data': data, 'count': data.count()})
    return render(request, "search.html", context={'data': None, 'count': 0})


# def home(request):
#     return render(request, "home.html")


# class HomeView(TemplateView):
#     template_name = "home.html"


# def contact(request):
#     return render(request, "contact.html")


class ContactView(TemplateView):
    template_name = "contact.html"


class MoviesView(ListView):
    template_name = "movies.html"
    model = Movie


class MovieCreateView(FormView):
    template_name = 'forms/new_movie_form.html'
    form_class = MovieForm
    success_url = reverse_lazy('create_movie')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Movie.objects.create(
            title=cleaned_data['title'],
            genre=cleaned_data['genre'],
            rating=cleaned_data['rating'],
            released=cleaned_data['released'],
            description=cleaned_data['description']
        )
        return result


class GenreCreateView(FormView):
    template_name = "forms/new_genre_form.html"
    form_class = GenreForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        new_genre = Genre(
            name=cleaned_data['name']
        )
        new_genre.save()
        return result


class GreetingView(View):
    greeting = "Good morning"

    def get(self, request):
        return HttpResponse(self.greeting)

