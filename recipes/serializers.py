from rest_framework import serializers

from .models import Follow, Favorite


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['id']
        model = Follow