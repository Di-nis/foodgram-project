from django import template
from api.models import Favorite, Purchase, Follow

register = template.Library()


@register.filter(name='is_favorite')
def is_favorite(recipe, user):
        return Favorite.objects.filter(user=user, recipe=recipe)

@register.filter(name='is_purchase')
def is_purchase(recipe, user):
        return Purchase.objects.filter(user=user, recipe=recipe)

@register.filter(name='is_subscribe')
def is_subscribe(author, user):
        return Follow.objects.filter(user=user, author=author)
