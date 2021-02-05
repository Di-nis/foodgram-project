from django.urls import include, path

from . import views

extra_patterns_recipe = [
    path("new/", views.new_recipe, name='new_recipe'),
    path("<int:recipe_id>/", views.recipe, name='recipe'),
    path("<int:recipe_id>/edit/", views.recipe_edit, name='recipe_edit'),
]

extra_patterns_my = [
    path("follow/", views.follow_index, name="follow_index"),
    path("favorite/", views.favorite_recipes, name='favorite_recipes'),
    path("?tags=<str:display_name>/", views.tag_filter, name="tag_filter"),
    path("shoplist/", views.shop_list, name='shop_list'),
    path("shoplist/download/", views.download, name='shop_list_download'),
]


urlpatterns = [
    path("", views.index, name="index"),
    path("?tags=<str:display_name>/", views.tag_filter, name="tag_filter"),
    path("recipe/", include(extra_patterns_recipe)),
    path("my/", include(extra_patterns_my)),
    # path("<str:username>/", views.profile, name='profile'),
    path("users/<int:id>/", views.profile, name='profile'),
]
