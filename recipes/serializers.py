from rest_framework import serializers

from .models import Follow, Favorite


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['id']
        model = Follow
    
    # def validate(self, data):
    #     if data['user'] == data['author']:
    #         raise serializers.ValidationError(
    #             "Вы не можете подписаться на самого себя")
