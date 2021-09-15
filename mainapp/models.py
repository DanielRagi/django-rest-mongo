from django.db import models


# Create your models here.
class MovieDetails(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    director = models.CharField(max_length=30)
    year = models.CharField(max_length=30)