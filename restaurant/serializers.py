from rest_framework import serializers
from .models import Restaurant, Menu

from datetime import date


class RestaurantSerializer(serializers.ModelSerializer):
    """Serializer for creating and viewing restaurant details."""

    class Meta:
        model = Restaurant
        fields = ["id", "name", "address", "cuisine_types"]


class MenuSerializer(serializers.ModelSerializer):
    """Serializer for creating and detail information of menu."""

    class Meta:
        model = Menu
        fields = ["id", "restaurant", "date", "dishes"]


class RestaurantListSerializer(serializers.ModelSerializer):
    """Serializer for listing restaurants (basic fields)."""

    class Meta:
        model = Restaurant
        fields = ["id", "name", "address"]



class MenuVoteCountSerializer(serializers.ModelSerializer):
    """Serializer for displaying menu with its vote count."""
    upvote_count = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ["id", "name", "upvote_count"]

    def get_upvote_count(self, obj):
        """Return the upvote count for the menu."""
        return obj.upvote_count
