from rest_framework import filters, permissions, viewsets
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from django.contrib.auth import get_user_model
from .models import Follow, Purchase, Favorite
from recipes.models import Ingredient
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from .permissions import IsStaffOrOwner
from .serializers import (FollowSerializer, 
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
    # filter_backends = [filters.SearchFilter]
    permission_classes = [IsStaffOrOwner, ]
    # search_fields = ['=name', ]
    # lookup_field = 'slug'



class SubscriptionsViewSet(CreateModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    # filter_backends = [filters.SearchFilter]
    permission_classes = [IsStaffOrOwner, ]
    # search_fields = ['=name', ]
    # lookup_field = 'slug'
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'recipes/MyFollow.html'

    # def get(self, request):
    #     user_list = User.objects.filter(following__user=request.user)
    #     paginator = Paginator(user_list, 3)
    #     page_number = request.GET.get('page')
    #     page = paginator.get_page(page_number)
    #     return Response({
    #         'page': page,
    #         'paginator': paginator
    #         }
    #     )


class FavoritesViewSet(CreateModelMixin, DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    # # filter_backends = [filters.SearchFilter]
    # permission_classes = [IsStaffOrOwner, ]
    # # search_fields = ['=name', ]
    # # lookup_field = 'slug'


class IngredientsViewSet(ListModelMixin, viewsets.GenericViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    search_fields = ['=name', ]