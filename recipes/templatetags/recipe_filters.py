from django import template

from api.models import Favorite, Follow, Purchase

register = template.Library()


@register.filter(name="is_favorite")
def is_favorite(recipe, user):
    return Favorite.objects.filter(user=user, recipe=recipe)


@register.filter(name="is_purchase")
def is_purchase(recipe, user):
    return Purchase.objects.filter(user=user, recipe=recipe)


@register.filter(name="is_subscribe")
def is_subscribe(author, user):
    return Follow.objects.filter(user=user, author=author)


@register.filter(name="is_not_user")
def is_not_user(user_profile, user):
    return user_profile is not user


@register.filter(name="addclass")
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter(name="display_name")
def display_name(user):
    if user.get_full_name() == "":
        return user.username
    return user.get_full_name()


@register.filter(name="parse_tags")
def parse_tags(get):
    return get.getlist("tag")


@register.filter(name="set_tag_qs")
def set_tag_qs(request, tag):
    new_req = request.GET.copy()
    tags = new_req.getlist("tag")
    if tag.display_name in tags:
        tags.remove(tag.display_name)
    else:
        tags.append(tag.display_name)

    new_req.setlist("tag", tags)
    return new_req.urlencode()
