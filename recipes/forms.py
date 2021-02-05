from django.db import models
from django import forms
# from django.forms import ModelForm

from .models import Ingredient, Recipe


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        exclude = ['author', 'slug']
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }


# class IngredientForm(ModelForm):
#     class Meta:
#         model = Ingredient
#         fields = '__all__'
