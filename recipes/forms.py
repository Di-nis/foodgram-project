from django.db import models
from django.forms import ModelForm, Textarea
from .models import Recipe, Ingredient


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        exclude = ['author', 'slug']
        # widgets = {
        #     'description': Textarea(attrs={'rows': 8,
        #                                    'label class': "form__label",
        #                                    'div class': 'form__field-group'}
        #     )
        # }


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'
