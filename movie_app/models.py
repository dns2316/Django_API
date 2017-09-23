from django.db import models

class Movie(models.Model):
    id_imdb = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.URLField(max_length=41)
    poster = models.URLField(max_length=225)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1500)
    year = models.SmallIntegerField()

    # def __str__(self):
    #     return self.name