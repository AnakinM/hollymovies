from logging import getLogger

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView, TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from viewer.forms import MovieForm, GenreForm
from viewer.models import Movie, Genre

LOG = getLogger()


def search(request):
    title = request.GET.get("title")
    if title:
        data = Movie.objects.filter(title__contains=title)
        return render(request, "search.html", context={'data': data, 'count': data.count()})
    return render(request, "search.html", context={'data': None, 'count': 0})


class StaffRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_staff


class ContactView(TemplateView):
    template_name = "contact.html"


class MovieDetailView(DetailView):
    template_name = "movie_detail_view.html"
    # queryset = Movie.objects.filter()
    model = Movie


class MoviesView(ListView):
    template_name = "movies.html"
    model = Movie
    paginate_by = 5


class MovieCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'forms/form.html'
    form_class = MovieForm
    success_url = reverse_lazy('viewer:movies')
    permission_required = 'viewer.add_movie'

    def form_invalid(self, form):
        LOG.warning("User provided invalid data.")
        return super().form_invalid(form)


class MovieUpdateView(LoginRequiredMixin, StaffRequiredMixin, UpdateView):
    template_name = "forms/form.html"
    form_class = MovieForm
    model = Movie
    success_url = reverse_lazy('viewer:movies')

    def form_invalid(self, form):
        LOG.warning("User provided invalid data while updating a movie.")
        return super().form_invalid(form)


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "forms/delete_movie_form.html"
    model = Movie
    success_url = reverse_lazy('viewer:movies')


class GenreCreateView(FormView):
    template_name = "forms/form.html"
    form_class = GenreForm
    success_url = reverse_lazy('viewer:genres')

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


class GenreUpdateView(UpdateView):
    template_name = "forms/form.html"
    form_class = GenreForm
    model = Genre
    success_url = reverse_lazy('viewer:genres')

    def form_invalid(self, form):
        LOG.warning("User provided invalid data while updating a genre.")
        return super().form_invalid(form)


class GreetingView(View):
    greeting = "Good morning"

    def get(self, request):
        return HttpResponse(self.greeting)
