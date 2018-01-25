from django.db import models


class RecipeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().union(super().get_queryset().using('newsstand'))
