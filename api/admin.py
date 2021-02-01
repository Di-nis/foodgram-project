from django.contrib import admin

from .models import Favorite, Follow, Purchase


class FollowAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "author")
    # list_filter = ("author", "name",)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "recipe")
    # list_filter = ("author", "name",)


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "recipe")
    # list_filter = ("author", "name",)


admin.site.register(Follow, FollowAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Purchase, PurchaseAdmin)
