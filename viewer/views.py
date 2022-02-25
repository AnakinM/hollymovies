from logging import getLogger

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView, TemplateView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from viewer.forms import MovieForm, GenreForm
from viewer.models import Movie, Genre

LOG = getLogger()


class StaffRequiredMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_staff


def search(request):
    title = request.GET.get("movie_title")
    if title:
        data = Movie.objects.filter(title__contains=title)
        return render(request, "search.html", context={'data': data, 'count': data.count(), 'movie_title': title})
    return render(request, "search.html", context={'data': None, 'count': 0, 'movie_title': ''})


# def home(request):
#     return render(request, "home.html")


class HomeView(TemplateView):
    template_name = "home.html"

    def get(self, request):
        movies_count = Movie.objects.all().count()
        genres_count = Genre.objects.all().count()
        users_count = User.objects.all().count()
        oldest_movie = Movie.objects.all().order_by("released").first()
        highest_rated_movie = Movie.objects.all().order_by("-rating").first()
        return render(request, "home.html", context={
            'movies_count': movies_count,
            'genres_count': genres_count,
            'users_count': users_count,
            'oldest_movie': oldest_movie,
            'highest_rated_movie': highest_rated_movie,
        })


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
    paginate_by = 6


class MovieCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'forms/form.html'
    form_class = MovieForm
    success_url = reverse_lazy('viewer:create_movie')
    permission_required = "viewer.add_movie"

    def form_invalid(self, form):
        LOG.warning("User provided invalid data.")
        return super().form_invalid(form)


class MovieUpdateView(PermissionRequiredMixin, StaffRequiredMixin, UpdateView):
    template_name = "forms/form.html"
    form_class = MovieForm
    model = Movie
    success_url = reverse_lazy('viewer:movies')
    permission_required = "viewer.change_movie"

    def form_invalid(self, form):
        LOG.warning("User provided invalid data while updating a movie.")
        return super().form_invalid(form)


class MovieDeleteView(PermissionRequiredMixin, StaffRequiredMixin, DeleteView):
    template_name = "forms/delete_movie_form.html"
    model = Movie
    success_url = reverse_lazy('viewer:movies')
    permission_required = "viewer.delete_movie"

    def test_func(self):
        return super().test_func() and self.request.user.is_superuser


class GenreListView(ListView):
    template_name = "genres.html"
    model = Genre


class GenreCreateView(PermissionRequiredMixin, FormView):
    template_name = "forms/form.html"
    form_class = GenreForm
    success_url = reverse_lazy('viewer:genres')
    permission_required = 'viewer.add_genre'

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        new_genre = Genre(
            name=cleaned_data['name']
        )
        new_genre.save()
        return result


class GenreUpdateView(PermissionRequiredMixin, StaffRequiredMixin, UpdateView):
    template_name = "forms/form.html"
    form_class = GenreForm
    model = Genre
    success_url = reverse_lazy('viewer:genres')
    permission_required = 'viewer.change_genre'

    def form_invalid(self, form):
        LOG.warning("User provided invalid data while updating a genre.")
        return super().form_invalid(form)


class GreetingView(View):
    greeting = "Good morning"

    def get(self, request):
        return HttpResponse(self.greeting)

# Add genre - Permission
# Update - Staff, Permission
