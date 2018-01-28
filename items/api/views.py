from rest_framework import viewsets

from items.api.serializers import SimpleItemSerializer, ItemSerializer
from ..models import Item


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-Only API view for the Item model
    """
    serializer_class = SimpleItemSerializer

    def get_serializer_context(self):
        return {'realm': self.request.query_params.get('realm', None)}

    def get_serializer(self, *args, **kwargs):
        """
        Switch serializer based on whether a realm is specified
        """
        kwargs['context'] = self.get_serializer_context()
        realm = kwargs['context']['realm']
        if realm is not None:
            serializer_class = ItemSerializer
        else:
            serializer_class = self.get_serializer_class()
        return serializer_class(*args, **kwargs)

    def get_queryset(self):
        queryset = Item.objects.all()
        name = self.request.query_params.get('name', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        return queryset
