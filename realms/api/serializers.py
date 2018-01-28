from rest_framework import serializers

from ..models import Realm


class RealmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realm
        fields = ('id', 'name', 'region', 'slug', 'house', 'population')
