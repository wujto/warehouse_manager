from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from warehouse_manager_base.models import ProductModel, CategoryModel, LocalizationModel

class ProductListView(ListView):
    model = ProductModel
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProductCreateView(CreateView):
    model = ProductModel
    fields = ['id_number', 'name', 'description', 'category','localization', 'photo']
    template_name = 'create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] ='product' 
        return context

class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ProductUpdateView(UpdateView):
    model = ProductModel
    template_name = 'edit.html'
    fields = ['name', 'description', 'category','localization', 'photo', 'product_set', 'product_user']

class ProductDeleteView(DeleteView):
    model = ProductModel
    success_url = reverse_lazy('product_list')
    template_name= 'delete.html'

class CategoryListView(ListView):
    model = CategoryModel
    template_name = 'list.html'

class CategoryCreateView(CreateView):
    model = CategoryModel
    fields = ['name','description']
    template_name = 'create.html'

class LocalizationCreateView(CreateView):
    model = LocalizationModel
    fields = ['name', 'description']
    template_name = 'create.html'