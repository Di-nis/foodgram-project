from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredient


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", )
    list_filter = ("name",)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("author", "name")
    list_filter = ("author", "name",)

class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ("ingredient", "amount")
    # list_filter = ("author", "name",)


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
