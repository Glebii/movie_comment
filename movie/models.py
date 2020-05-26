from django.db import models
from django.utils import timezone


 
# Create your models here.
class Genre(models.Model):
    title = models.CharField(max_length=30)
    


class Movie(models.Model):
    title = models.CharField(max_length=120)
    pop = models.FloatField()
    cast = models.ManyToManyField('actor.Actor')
    overview = models.TextField()
    genres = models.ManyToManyField(Genre)
    poster = models.ImageField(upload_to='/movies/posters',max_length=100)
    budget = models.IntegerField()
    release_date = models.DateField(auto_now=False,auto_now_add=False)
    movie_duration = models.PositiveSmallIntegerField()
    company = models.TimeField()
    


class Comment(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    