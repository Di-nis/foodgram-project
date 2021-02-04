from rest_framework import serializers

from .models import Favorite, Follow, Purchase
from recipes.models import Ingredient



# class CustomModelSerializer(serializers.ModelSerializer):
#     def create(self, validated_data):
#         validated_data['user'] = self.context['request'].user
#         return self.Meta.model.objects.create(**validated_data)


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        # fields = ['user', 'author']
        fields = ('author', )
        model = Follow
    
    # def validate(self, data):
    #     print(self.context['request'].user)
    #     return data
    #     print('печать', data)
    #     print(data['author'])
    #     if data['user'] == data['author']:
    #         raise serializers.ValidationError(
    #             "Вы не можете подписаться на самого себя")
    #     return data


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
