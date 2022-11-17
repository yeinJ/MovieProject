from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie, Review

# Create your models here.
class User(AbstractUser):
    like_movies = models.ManyToManyField(Movie, related_name = 'movie_like_users') 
    like_reviews = models.ManyToManyField(Review, related_name = 'review_like_users')