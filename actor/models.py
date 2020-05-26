from django.db import models
from movie.models import Movie
# Create your models here.
class Actor(models.Model):
    birthday = models.DateField(auto_now=False, auto_now_add=False)
    deathday = models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    actor_name = models.CharField(max_length=40)
    place_of_birth = models.TextField()
    movies = models.ManyToManyField('Movie',related_name='actors')