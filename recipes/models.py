from django.db import models

from .managers import RecipeManager


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(
        max_length=128
    )

    description = models.CharField(
        max_length=512
    )

    cooldown = models.IntegerField(
        default=0
    )

    skillline = models.SmallIntegerField()

    qtymade = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0.00
    )

    crafteditem = models.PositiveIntegerField()

    expansion = models.PositiveSmallIntegerField()

    objects = RecipeManager()

    class Meta:
        db_table = 'tblDBCSpell'
        ordering = ['id']
