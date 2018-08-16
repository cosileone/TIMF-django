from django.db.models import QuerySet


class RealmQuerySet(QuerySet):
    def connected(self, house_id):
        return self.filter(house=house_id)

