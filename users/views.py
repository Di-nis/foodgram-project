from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("signup_done")
    template_name = "users/reg.html"


class SignUpDoneView(TemplateView):
    template_name = 'users/signup_done.html'
