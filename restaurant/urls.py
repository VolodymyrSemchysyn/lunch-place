from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.views import RestaurantViewSet, MenuViewSet, MenuVoteCountListView


router = DefaultRouter()
router.register("restaurants", RestaurantViewSet)
router.register("menus", MenuViewSet, basename="menu")

urlpatterns = [
    path("", include(router.urls)),
    path("menu-votes/", MenuVoteCountListView.as_view(), name="menu-vote"),
]

app_name = "restaurant"