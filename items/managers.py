from django.db import models


class ItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(auctionable=1).using('newsstand')
