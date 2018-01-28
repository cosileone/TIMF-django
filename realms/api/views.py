from rest_framework import viewsets, pagination

from realms.api.serializers import RealmSerializer
from ..models import Realm


class BigResultsList(pagination.PageNumberPagination):
    page_size = 1000


class RealmViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-Only endpoint for the Realm List
    """

    queryset = Realm.objects.filter(region__in=['US', 'EU'])
    serializer_class = RealmSerializer
    pagination_class = BigResultsList
