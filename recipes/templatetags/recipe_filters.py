from django import template

from api.models import Favorite, Follow, Purchase

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


@register.filter(name='is_not_user')
def is_not_user(user_profile, user):
    return user_profile is not user


@register.filter(name='addclass')
def addclass(field, css):
    return field.as_widget(attrs={'class': css})
