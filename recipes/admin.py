from django.contrib import admin

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
    list_display = ['reagent', 'quantity', 'spell', 'item']
    list_display_links = None
    search_fields = ['item__name', 'spell__name', 'reagent__name']
    ordering = ['spell']
