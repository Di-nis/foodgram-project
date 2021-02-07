from django.contrib.auth import get_user_model
from rest_framework import filters, permissions, viewsets
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.response import Response

from recipes.models import Ingredient, RecipeIngredient

from .models import Favorite, Follow, Purchase
from .serializers import (FavoriteSerializer, IngredientSerializer,
                          PurchaseSerializer, SubscriptionSerializer)

User = get_user_model()

class BaseCreateListDestroyViewSet(
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class PurchasesViewSet(BaseCreateListDestroyViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    lookup_field = 'recipe_id'



class SubscriptionsViewSet(CreateModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Follow.objects.all()
    serializer_class = SubscriptionSerializer
    # filter_backends = [filters.SearchFilter]
    permission_classes = (permissions.IsAuthenticated, )
    # search_fields = ['=name', ]
    lookup_field = 'author'


class FavoritesViewSet(CreateModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    # # search_fields = ['=name', ]
    lookup_field = 'recipe'


class IngredientsViewSet(ListModelMixin, viewsets.GenericViewSet):
    queryset = Ingredient.objects.all()
    # queryset = RecipeIngredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [permissions.AllowAny, ]
    search_fields = ['name', ]
    # filterset_fields = ['name',]
