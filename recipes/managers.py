from django.db import models
from itertools import chain


class RecipeManager(models.Manager):
    def get_queryset(self):
        default_results = super(RecipeManager, self).get_queryset().using('default').exclude(skillline__isnull=True)
        newsstand_results = super(RecipeManager, self).get_queryset().exclude(skillline__isnull=True)
        return newsstand_results.order_by('id').union(default_results.order_by('id'))
