from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredient, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "display_name", "color")


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "dimension")
    list_filter = ("name", )
    search_fields = ("name", )


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "title")
    list_filter = ("author", "title",)


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ("id", "ingredient", "recipe", "amount")
    search_fields = ("ingredient__name", "recipe__title")


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
