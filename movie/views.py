from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from .models import Genre, Movie
from .tmdb_utils import get_movie_by_id

# Create your views here.


def create_by_id_view(req: HttpRequest):
    tmdb_id = req.GET.get("tmdb_id")
    movie_data = get_movie_by_id(int(tmdb_id))
    genres = Genre.objects.filter(title__in=[g.get("name") for g in movie_data["genres"]])
    for i in movie_data["genres"]:
        if i not in movie_data["genres"]:
            new_genre = Genre.object.create(title=i.get("name"))
            Movie.genres.add(new_genre)
    movie = Movie(
        title=movie_data["original_title"],
        pop=movie_data["popularity"],
        overview=movie_data["overview"],
        genres=[g.get("name") for g in movie_data["genres"]],
        budget=movie_data["budget"],
        release_date=movie_data["release_date"],
        movie_duration=movie_data["runtime"],
        company=
    )
    movie.save()
    return JsonResponse({"title": movie.title, "id": movie.id, "genre": movie.genres})


