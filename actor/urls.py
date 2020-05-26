from django.urls import path
from .views import create_actor_by_id_view

urlpatterns = [
    path('create_actor_by_id', create_actor_by_id_view),
]