from django.contrib.auth.forms import UserCreationForm
# from .models import User
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext, gettext_lazy as _

User = get_user_model()

class CreationForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             label=_("Электронная почта"),
                            #  widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
                            #  strip=False,
                             help_text=_("Введите адрес электронной почты"),
    )


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", )

        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form__input'})
        }
