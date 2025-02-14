from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.views import RestaurantViewSet, MenuViewSet, MenuVoteCountListView


router = DefaultRouter()
router.register("restaurants", RestaurantViewSet)
router.register("menus", MenuViewSet, basename="menu")

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v2/", include(router.urls)),
    path("v1/menu-votes/", MenuVoteCountListView.as_view(), name="menu-vote"),
    path("v2/menu-votes/", MenuVoteCountListView.as_view(), name="menu-vote"),
]

app_name = "restaurant"
