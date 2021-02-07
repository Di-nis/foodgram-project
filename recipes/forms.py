from django import forms
from django.db import models

from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        # exclude = ['author', 'slug', 'pub_date']
        fields = ['title', 'ingredients', 'prep_time', 'description', 'image']
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }
