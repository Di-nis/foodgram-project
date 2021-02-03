from rest_framework import filters, permissions, viewsets
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from django.contrib.auth import get_user_model
from .models import Follow, Purchase, Favorite
from recipes.models import Ingredient
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .permissions import IsStaffOrOwner
from .serializers import (SubscriptionSerializer, 
                          PurchaseSerializer, 
                          FavoriteSerializer,
                          IngredientSerializer)


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
    # filter_backends = [filters.SearchFilter]
    # permission_classes = [IsStaffOrOwner, ]
    # search_fields = ['=name', ]
    lookup_field = 'recipe__id'



class SubscriptionsViewSet(CreateModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Follow.objects.all()
    serializer_class = SubscriptionSerializer
    # filter_backends = [filters.SearchFilter]
    permission_classes = (permissions.IsAuthenticated, )
    # permission_classes = [IsStaffOrOwner, ]
    # search_fields = ['=name', ]
    lookup_field = 'author'


class FavoritesViewSet(CreateModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    # # filter_backends = [filters.SearchFilter]
    # permission_classes = [IsStaffOrOwner, ]
    # # search_fields = ['=name', ]
    lookup_field = 'recipe'


class IngredientsViewSet(ListModelMixin, viewsets.GenericViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [permissions.AllowAny, ]
    # search_fields = ['name', ]
    # filterset_fields = ['text',]
