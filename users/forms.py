from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class CreationForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             label=_("Электронная почта"),
                             help_text=_("Введите адрес электронной почты"),
                             )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", )
