from django.db.models import QuerySet, Q, F, Avg, Min, Max, Sum, FloatField

from realms.models import Realm
from .utils import median_value


class AuctionQuerySet(QuerySet):
    def available_to(self, realm):
        if not isinstance(realm, Realm):
            realm = Realm.objects.get(id=realm)

        connected = Realm.objects.connected(realm.house)
        return self.filter(ownerRealm__in=connected)

    def non_zero_buyouts(self):
        return self.filter(Q(buyout__gt=0))

    def bid_stats(self):
        bid_min = Min(F('bid')/F('quantity'), output_field=FloatField())
        bid_max = Max(F('bid')/F('quantity'), output_field=FloatField())
        bid_avg = Avg(F('bid')/F('quantity'), output_field=FloatField())

        total_available_units = Sum('quantity')
        total_market_cap = Sum('bid')
        return self.non_zero_buyouts().aggregate(
            bid_min=bid_min,
            bid_max=bid_max,
            bid_avg=bid_avg,
            total_units=total_available_units,
            market_cap=total_market_cap
        )

    def buyout_stats(self):
        buyout_min = Min(F('buyout')/F('quantity'), output_field=FloatField())
        buyout_max = Max(F('buyout')/F('quantity'), output_field=FloatField())
        buyout_avg = Avg(F('buyout')/F('quantity'), output_field=FloatField())

        total_available_units = Sum('quantity')
        total_market_cap = Sum('buyout')
        return self.non_zero_buyouts().aggregate(
            buyout_min=buyout_min,
            buyout_max=buyout_max,
            buyout_avg=buyout_avg,
            total_units=total_available_units,
            market_cap=total_market_cap
        )

    def buyout_median(self):
        return median_value(self.non_zero_buyouts(), 'buyout')

    def bid_median(self):
        return median_value(self, 'bid')

