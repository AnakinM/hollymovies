from django.urls import path

from viewer.views import MoviesView, MovieCreateView, GenreCreateView, MovieUpdateView, MovieDeleteView, \
    MovieDetailView, GenreListView, GenreUpdateView

app_name = 'viewer'
urlpatterns = [
    path('', MoviesView.as_view(), name="movies"),
    path('new/', MovieCreateView.as_view(), name="create_movie"),
    path('<int:pk>/', MovieDetailView.as_view(), name="read_movie"),
    path('<int:pk>/update/', MovieUpdateView.as_view(), name="update_movie"),
    path('<int:pk>/delete/', MovieDeleteView.as_view(), name="delete_movie"),
    path('genres/', GenreListView.as_view(), name="genres"),
    path('genres/new/', GenreCreateView.as_view(), name="create_genre"),
    path('genres/<int:pk>/update/', GenreUpdateView.as_view(), name="update_genre"),
]
