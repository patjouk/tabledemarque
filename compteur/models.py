from django.db import models

class Jeux(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    jeux = models.SlugField(unique=True)