from rest_framework import serializers

from .models import Favorite, Follow, Purchase
from recipes.models import Ingredient





class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        # fields = ['user', 'author']
        fields = ('author', )
        model = Follow
    
    def validate(self, data):
        if data['user'] == data['author']:
            raise serializers.ValidationError(
                "Вы не можете подписаться на самого себя")
        return data


class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('recipe', )
        model = Purchase


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        # fields = ['user', 'recipe']
        fields = ('recipe', )
        model = Favorite


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'dimension']
        model = Ingredient
