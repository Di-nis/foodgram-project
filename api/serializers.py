from rest_framework import serializers

from recipes.models import Ingredient

from .models import Favorite, Follow, Purchase


class CustomSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


class SubscriptionSerializer(CustomSerializers):

    class Meta:
        fields = ["user", "author"]
        model = Follow

    def validate(self, data):
        if data["user"] == data["author"]:
            raise serializers.ValidationError(
                "Вы не можете подписаться на самого себя")
        return data


class PurchaseSerializer(CustomSerializers):

    class Meta:
        fields = ["user", "recipe"]
        model = Purchase


class FavoriteSerializer(CustomSerializers):

    class Meta:
        fields = ["user", "recipe"]
        model = Favorite


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Ingredient
