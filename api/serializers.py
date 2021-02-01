from rest_framework import serializers

from .models import Favorite, Follow, Purchase
from recipes.models import Ingredient


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['user', 'author']
        model = Follow
    
    def validate(self, data):
        if data['user'] == data['author']:
            raise serializers.ValidationError(
                "Вы не можете подписаться на самого себя")
        return data


class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['user', 'recipe']
        model = Purchase


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['user', 'recipe']
        model = Favorite


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'dimension']
        model = Ingredient