from django.db import models
from django.conf import settings

# Create your models here.
from django.db import models

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    trailer_path = models.CharField(max_length=200)
    star_rating_average = models.FloatField(default=5)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Collection(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)
    title = models.CharField(max_length=100)
    info = models.CharField(max_length=200)

    def __str__(self):
        return self.title
