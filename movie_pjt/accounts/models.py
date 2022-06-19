from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    region = models.CharField(max_length=20)
    genre_like = models.CharField(max_length=20)
    genre_dislike = models.CharField(max_length=20)