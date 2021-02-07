from django.contrib.auth import get_user_model
from rest_framework import filters, permissions, viewsets
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)

from recipes.models import Ingredient

from .models import Favorite, Follow, Purchase
from .serializers import (FavoriteSerializer, IngredientSerializer,
                          PurchaseSerializer, SubscriptionSerializer)

User = get_user_model()


class BaseCreateDestroyViewSet(
    CreateModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class PurchasesViewSet(BaseCreateDestroyViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    lookup_field = 'recipe_id'


class SubscriptionsViewSet(BaseCreateDestroyViewSet):
    queryset = Follow.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = 'author'


class FavoritesViewSet(BaseCreateDestroyViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    lookup_field = 'recipe'


class IngredientsViewSet(ListModelMixin, viewsets.GenericViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [permissions.AllowAny, ]
    search_fields = ['name', ]
