from django.db import models


class RecipeQuerySet(models.QuerySet):
    def crafted(self):
        default_results = self.using('default').exclude(skillline__isnull=True)
        newsstand_results = self.exclude(skillline__isnull=True)
        return newsstand_results.order_by('id').union(default_results.order_by('id'))
