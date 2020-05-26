from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from .models import Actor
from .tmdb_actor_utils import get_actor_by_id

# Create your views here.


def create_actor_by_id_view(req:HttpRequest):
    tmdb_actor_id = req.GET.get("tmdb_actor_id")
    actor_data=  get_actor_by_id(int(tmdb_actor_id))
    # actor = Actor(title=movie_data["original_title"], pop=movie_data["popularity"], overview=movie_data["overview"])
    # movie.save()
    # return JsonResponse({
    #     "title": movie.title,
    #     "id": movie.id
    # })