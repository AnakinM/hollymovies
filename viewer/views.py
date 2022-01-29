from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, TemplateView

from viewer.forms import MovieForm
from viewer.models import Movie


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
    template_name = 'form.html'
    form_class = MovieForm
