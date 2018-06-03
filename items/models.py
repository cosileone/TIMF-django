from django.db import models

from .managers import ItemManager


# Create your models here.
class Item(models.Model):
    blizzard_id = models.IntegerField(
        null=True,
        default=None
    )

    name = models.CharField(
        max_length=250,
        db_column='name_enus'
    )
    quality = models.SmallIntegerField()

    level = models.SmallIntegerField(
        null=True,
        default=None
    )

    item_class = models.SmallIntegerField(
        db_column='class'
    )
    subclass = models.SmallIntegerField()
    icon = models.CharField(max_length=120)

    stacksize = models.SmallIntegerField(
        null=True,
        default=None
    )

    buyfromvendor = models.IntegerField(
        blank=True,
        null=True,
        default=None
    )
    selltovendor = models.IntegerField(
        blank=True,
        null=True,
        default=None
    )

    auctionable = models.SmallIntegerField(
        null=True,
        default=None
    )

    type = models.SmallIntegerField(
        null=True,
        default=None
    )

    requiredlevel = models.SmallIntegerField(
        null=True,
        default=None
    )

    requiredskill = models.SmallIntegerField(
        null=True,
        default=None
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
