from rest_framework import serializers

from ..models import Item

from django.db.models import Avg, Max, Min, F, FloatField, Sum


class SimpleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['blizzard_id', 'name']


class ItemSerializer(serializers.ModelSerializer):
    market_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Item
        fields = ['id', 'blizzard_id', 'name', 'selltovendor', 'market_data']

    def get_market_data(self, obj):
        realm = self.context.get('realm')
        buyout_min = Min(F('buyout') / F('quantity'), output_field=FloatField())
        buyout_max = Max(F('buyout') / F('quantity'), output_field=FloatField())
        buyout_avg = Avg(F('buyout') / F('quantity'), output_field=FloatField())

        total_available_units = Sum('quantity')
        total_market_cap = Sum('buyout')

        return obj.auctions.available_to(realm).buyout_stats().aggregate(
            buyout_min=buyout_min,
            buyout_max=buyout_max,
            buyout_avg=buyout_avg,
            total_units=total_available_units,
            market_cap=total_market_cap
        )
