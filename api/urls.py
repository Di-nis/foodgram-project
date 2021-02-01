from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FavoritesViewSet, SubscriptionsViewSet, PurchasesViewSet

v1_router = DefaultRouter()
v1_router.register('subscriptions', SubscriptionsViewSet, 'subscriptions')
v1_router.register('favorites', FavoritesViewSet, basename='favorites')
v1_router.register('purchases', PurchasesViewSet, 'purchases')



urlpatterns = [
    path("v1/", include(v1_router.urls)),
]
