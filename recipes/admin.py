from django.contrib import admin

from .models import (Ingredient, Recipe, RecipeIngredient, 
                     Follow, Favorite, Purchase)


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", )
    list_filter = ("name",)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("author", "name")
    list_filter = ("author", "name",)

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ("ingredient", "amount")
    # list_filter = ("author", "name",)


class FollowAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "author")
    # list_filter = ("author", "name",)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("user", "recipe")
    # list_filter = ("author", "name",)


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("user", "recipe")
    # list_filter = ("author", "name",)

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Purchase, PurchaseAdmin)
