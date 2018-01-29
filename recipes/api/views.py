from rest_framework import viewsets

from recipes.api.serializers import RecipeSerializer
from ..models import Recipe


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API view for the Recipe model
    """
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.exclude(skillline__isnull=True)
