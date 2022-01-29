from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from viewer.forms import MovieForm
from viewer.models import Movie


def search(request):
    data = request.GET.get("title")
    return HttpResponse(f"You looked for {data}")


class MoviesView(ListView):
    template_name = "movies.html"
    model = Movie


class MovieCreateView(FormView):
    template_name = 'form.html'
    form_class = MovieForm
