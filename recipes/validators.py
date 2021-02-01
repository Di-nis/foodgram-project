from django.core.exceptions import ValidationError


def validate_follow(user, author):
    if user == author:
        raise ValidationError('Вы не можете подписаться на самого себя')
