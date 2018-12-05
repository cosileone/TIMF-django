from rest_framework import serializers

from ..models import Item


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
        return obj.auctions.available_to(realm).buyout_stats().aggregate(
            market_cost_buyout=Sum(F('buyout_min')*F('quantity'), output_field=IntegerField())
        )
