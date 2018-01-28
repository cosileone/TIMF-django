from rest_framework import viewsets

from items.api.serializers import ItemSerializer
from ..models import Item


class ItemViewSet(viewsets.ModelViewSet):
    """
    API view for the Item model
    """
    queryset = Item.all
    serializer_class = ItemSerializer
