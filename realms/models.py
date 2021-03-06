from django.db import models

from .managers import RealmQuerySet


# Create your models here.
class Realm(models.Model):
    REGIONS = (
        ('US', 'US'),
        ('EU', 'EU'),
        ('CN', 'CN'),
        ('TW', 'TW'),
        ('KR', 'KR')
    )

    name = models.CharField(
        max_length=100
    )

    region = models.CharField(
        max_length=2,
        choices=REGIONS
    )

    slug = models.CharField(
        max_length=100
    )

    house = models.PositiveSmallIntegerField(blank=True, null=True)
    population = models.PositiveIntegerField(blank=True, null=True)

    objects = RealmQuerySet.as_manager()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '{} ({})'.format(self.slug, self.region)
