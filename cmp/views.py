from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Proveedor
from cmp.forms import ProveedorForm
 
class ProveedorView(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    tempalte_name = "cmp/proveedor_list.html"
    context_object_name = "obj"
    login_url = "bases:login"
    
class ProveedorNew(LoginRequiredMixin, generic.CreateView):
    model = Proveedor
    tempalte_name = "cmp/proveedor_form.html"
    context_object_name = "obj"
    form_class = ProveedorForm
    success_url = reverse_lazy("cmp:proveedor_list")
    login_url = "bases:login"
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class ProveedorEdit(LoginRequiredMixin,
                   generic.UpdateView):
    model=Proveedor
    template_name="cmp/proveedor_form.html"
    context_object_name = 'obj'
    form_class = ProveedorForm
    success_url= reverse_lazy("cmp:proveedor_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)     
    
    
    
       
    
    
