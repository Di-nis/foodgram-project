from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'prep_time', 'description', 'image']
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }
