from django.urls import include, path

from . import views

extra_patterns_recipe = [
    path("new/", views.new_recipe, name="new_recipe"),
    path("<int:recipe_id>/", views.recipe, name="recipe"),
    path("<int:recipe_id>/edit/", views.recipe_edit, name="recipe_edit"),
    path("<int:recipe_id>/delete/", views.recipe_delete, name="recipe_delete"),
]

extra_patterns_my = [
    path("follow/", views.follow_index, name="follow_index"),
    path("favorite/", views.favorite_recipes, name="favorite_recipes"),
    path("shoplist/", views.shop_list, name="shop_list"),
    path("shoplist/download/", views.download, name="shop_list_download"),
]


urlpatterns = [
    path("", views.index, name="index"),
    path("recipe/", include(extra_patterns_recipe)),
    path("my/", include(extra_patterns_my)),
    path("<str:username>/", views.profile, name="profile"),
]
