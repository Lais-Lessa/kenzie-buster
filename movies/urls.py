from django.urls import path
from movies.views import MovieView, MovieDetailView

urlpatterns = [
    path('movies/', MovieView.as_view(), name='movie-list'),
    path('movies/<int:movie_id>/', MovieDetailView.as_view(), name='movie-detail'),
]
