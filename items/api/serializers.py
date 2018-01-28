from rest_framework import serializers

from ..models import Item


class SimpleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'selltovendor')
