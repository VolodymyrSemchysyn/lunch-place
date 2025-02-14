import datetime

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from restaurant.mixins import VersionedAPIView
from restaurant.models import Restaurant, Menu
from restaurant.permissions import IsAdminOrIfAuthenticatedReadOnly
from restaurant.serializers import RestaurantSerializer, RestaurantListSerializer, MenuSerializer, \
    MenuVoteCountSerializer


class RestaurantViewSet(VersionedAPIView, ModelViewSet):
    queryset = Restaurant.objects.all()
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]

    def get_serializer_class(self):
        if self.action == "list":
            return RestaurantListSerializer
        return RestaurantSerializer


class MenuViewSet(VersionedAPIView, ModelViewSet):
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]
    serializer_class = MenuSerializer

    def get_queryset(self):
        today = datetime.date.today()
        return Menu.objects.filter(date=today).select_related("restaurant")

class MenuVoteCountListView(VersionedAPIView, generics.ListAPIView):
    """View to list all menus with their upvote counts."""
    serializer_class = MenuVoteCountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        today = datetime.date.today()
        return Menu.objects.filter(date=today).select_related("restaurant").prefetch_related("votes")
