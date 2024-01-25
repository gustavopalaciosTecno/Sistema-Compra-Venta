from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Categoria

class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = 'inv/categoria_list.html'
    context_object_name = "obj"
    login_url = 'bases:login'

