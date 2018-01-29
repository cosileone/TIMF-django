from rest_framework import serializers

from ..models import Recipe
from items.models import Item


class ReagentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name')


class RecipeSerializer(serializers.ModelSerializer):
    reagents = ReagentSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'cooldown', 'skillline', 'qtymade', 'reagents')
