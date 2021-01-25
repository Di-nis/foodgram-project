from django.db import models
from django.forms import ModelForm, Textarea
from .models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        # fields = '__all__'
        exclude = ['author', 'slug']
        widgets = {
            'description': Textarea(attrs={'rows': 8}),
        }
