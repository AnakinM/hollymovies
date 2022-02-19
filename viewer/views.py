from logging import getLogger

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView, TemplateView, CreateView, UpdateView, DeleteView, DetailView

from viewer.forms import MovieForm, GenreForm
from viewer.models import Movie, Genre

LOG = getLogger()


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


class MovieDetailView(DetailView):
    template_name = "movie_detail_view.html"
    # queryset = Movie.objects.filter()
    model = Movie


class MoviesView(ListView):
    template_name = "movies.html"
    model = Movie


class MovieCreateView(CreateView):
    template_name = 'forms/form.html'
    form_class = MovieForm
    success_url = reverse_lazy('create_movie')

    def form_invalid(self, form):
        LOG.warning("User provided invalid data.")
        return super().form_invalid(form)


class MovieUpdateView(UpdateView):
    template_name = "forms/form.html"
    form_class = MovieForm
    model = Movie
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        LOG.warning("User provided invalid data while updating a movie.")
        return super().form_invalid(form)


class MovieDeleteView(DeleteView):
    template_name = "forms/delete_movie_form.html"
    model = Movie
    success_url = reverse_lazy('index')


class GenreCreateView(FormView):
    template_name = "forms/form.html"
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


class GenreListView(ListView):
    template_name = "genres.html"
    model = Genre


class GreetingView(View):
    greeting = "Good morning"

    def get(self, request):
        return HttpResponse(self.greeting)

# Listowanie gatunków filmów
# Updatowanie danego gatunku filmu
