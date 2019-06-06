from rest_framework import serializers
from apps.menu_items.models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ('id', 'name', 'price')
