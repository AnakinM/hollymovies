from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from viewer.forms import MovieForm
from viewer.models import Movie


def search(request):
    title = request.GET.get("title")
    if title:
        movies = Movie.objects.filter(title__contains=title)
        return render(request, "search.html", context={"movies": movies, "count": movies.count()})
    return render(request, "search.html", context={"movies": None, "count": 0})


class MoviesView(ListView):
    template_name = "movies.html"
    model = Movie


class MovieCreateView(FormView):
    template_name = 'form.html'
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
            description=cleaned_data['description'],
        )
        return result
