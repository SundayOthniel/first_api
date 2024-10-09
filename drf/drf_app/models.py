from django.db import models

class Movies(models.Model):
    genre = models.CharField(max_length=255)
    release_year = models.IntegerField()
    min_rating = models.IntegerField()
    director = models.CharField(max_length=255)

    class Meta:
        db_table = 'movies'
