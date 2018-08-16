from django.db.models import QuerySet

from realms.models import Realm


class AuctionQuerySet(QuerySet):
    def available_to(self, realm_id):
        realm = Realm.objects.get(id=realm_id)
        connected = Realm.objects.connected(realm.house)
        return self.filter(ownerRealm__in=connected)

