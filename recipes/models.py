from django.db import models


# Create your models here.
class Recipe(models.Model):
    blizzard_id = models.IntegerField(
        null=True,
        default=None
    )

    name = models.CharField(
        max_length=128
    )

    description = models.CharField(
        verbose_name='Spell Description',
        max_length=512
    )

    cooldown = models.IntegerField(
        default=0
    )

    skillline = models.SmallIntegerField(
        blank=True,
        null=True,
        default=None
    )

    qtymade = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        default=0.00
    )

    crafteditem = models.ForeignKey(
        'items.Item',
        related_name='crafting_recipe',
        verbose_name='Crafted Item',
        db_column='crafteditem',
        on_delete=models.PROTECT,
    )

    reagents = models.ManyToManyField(
        'items.Item',
        through='Ingredient',
        through_fields=('spell', 'reagent'),
        related_name='recipes',
    )

    expansion = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        default=None
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']

    # def save(self, *args, **kwargs):
    #     ingredient = Ingredient.objects.create(item=self.crafteditem, spell=self)
    #     return super(Recipe, self).save(*args, **kwargs)


class Ingredient(models.Model):
    item = models.ForeignKey(
        'items.Item',
        on_delete=models.PROTECT,
        db_column='item',
        related_name='reagent_for',
        verbose_name='Item Made'
    )

    skillline = models.PositiveSmallIntegerField()

    reagent = models.ForeignKey(
        'items.Item',
        on_delete=models.PROTECT,
        db_column='reagent'
    )
    quantity = models.DecimalField(max_digits=8, decimal_places=4)

    spell = models.ForeignKey(
        'Recipe',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.reagent.name

    class Meta:
        ordering = ['spell']
        unique_together = [('reagent', 'spell')]
