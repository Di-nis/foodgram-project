from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (FavoritesViewSet, IngredientsViewSet, PurchasesViewSet,
                    SubscriptionsViewSet)

v1_router = DefaultRouter()
v1_router.register("subscriptions", SubscriptionsViewSet, "subscriptions")
v1_router.register("favorites", FavoritesViewSet, "favorites")
v1_router.register("purchases", PurchasesViewSet, "purchases")
v1_router.register("ingredients", IngredientsViewSet, "ingredients")


urlpatterns = [
    path("v1/", include(v1_router.urls)),
]
