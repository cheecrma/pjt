from django.db import models
from django.conf import settings

# Create your models here.
class Movierate(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.CharField(max_length=100)
    poster_path = models.TextField()
    genre_ids = models.JSONField()
    vote_average = models.FloatField()

    def __str__(self):
        return self.title


class Rate(models.Model):
    star_rate = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    movierate = models.ForeignKey(Movierate, on_delete = models.CASCADE, related_name='rates')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.star_rate