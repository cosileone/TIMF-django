from django.db import models


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

    house = models.SmallIntegerField()
    population = models.IntegerField()

    class Meta:
        db_table = 'tblRealm'
        ordering = ['id']
