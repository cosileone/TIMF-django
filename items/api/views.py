from rest_framework import viewsets, filters

from items.api.serializers import SimpleItemSerializer, ItemSerializer
from ..models import Item

from realms.models import Realm


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-Only API view for the Item model
    """
    serializer_class = SimpleItemSerializer
    lookup_field = 'blizzard_id'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def get_serializer_context(self):
        context = super(ItemViewSet, self).get_serializer_context()
        region = self.request.query_params.get('region', 'US')
        realm_slug = self.request.query_params.get('realm', None)
        if realm_slug:
            context['realm'] = Realm.objects.get(slug=realm_slug, region=region)
        return context

    def get_serializer(self, *args, **kwargs):
        """
        Switch serializer based on whether a realm is specified
        """
        kwargs['context'] = self.get_serializer_context()
        realm = kwargs['context'].get('realm', None)
        if realm is not None:
            serializer_class = ItemSerializer
        else:
            serializer_class = self.get_serializer_class()
        return serializer_class(*args, **kwargs)

    def get_queryset(self):
        queryset = Item.objects.filter(auctionable=True)

        return queryset
