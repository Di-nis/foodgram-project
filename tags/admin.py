from django.contrib import admin
from .models import Tag

class TagAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    # list_filter = ("name",)


admin.site.register(Tag, TagAdmin)
