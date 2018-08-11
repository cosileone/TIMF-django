from rest_framework import serializers

from items.models import Item


class SimpleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('blizzard_id', 'name')


class ItemSerializer(serializers.ModelSerializer):
    auction_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Item
        fields = ('blizzard_id', 'name', 'selltovendor', 'auction_data')

    def get_auction_data(self, obj):
        return obj
