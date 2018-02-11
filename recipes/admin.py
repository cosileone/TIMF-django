from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Recipe, Ingredient


class ReagentInline(admin.TabularInline):
    readonly_fields = ['reagent', 'quantity']
    exclude = ['skillline', 'item']
    model = Ingredient
    extra = 10


# Register your models here.
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'qtymade', 'cooldown', 'skillline']
    inlines = [ReagentInline]
    list_display = ['name', 'crafteditem', 'qtymade']
    list_display_links = ['name', 'crafteditem']
    search_fields = ['name', 'crafteditem__name']
    autocomplete_fields = ['crafteditem']
    ordering = ['id']


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['reagent_link', 'quantity', 'spell_link', 'item_link']
    list_select_related = (
        'reagent', 'spell', 'item'
    )
    list_display_links = None
    search_fields = ['item__name', 'spell__name', 'reagent__name']
    ordering = ['spell']

    def spell_link(self, obj):
        return mark_safe('<a href="{0}">{1}</a>'.format(
            reverse('admin:recipes_recipe_change', args=(obj.pk,)),
            obj.spell
        ))

    spell_link.short_description = 'Recipe'

    def item_link(self, obj):
        return mark_safe('<a href="{0}">{1}</a>'.format(
            reverse('admin:items_item_change', args=(obj.item.pk,)),
            obj.item
        ))
    item_link.short_description = 'Item'

    def reagent_link(self, obj):
        return mark_safe('<a href="{0}">{1}</a>'.format(
            reverse('admin:items_item_change', args=(obj.reagent.pk,)),
            obj.reagent
        ))
    reagent_link.short_description = 'Reagent'
