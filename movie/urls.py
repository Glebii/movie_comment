from django.urls import path
from .views import create_by_id_view

urlpatterns = [
    path('create_movie_by_id', create_by_id_view),
]