from django.db import models

from .managers import RecipeManager


# Create your models here.
class Recipe(models.Model):
    objects = RecipeManager()
