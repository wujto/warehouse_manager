from django.shortcuts import render
from django.views.generic.list import ListView

from warehouse_manager_base.models import ProductModel

class ProductListView(ListView):
    model = ProductModel
    template_name = 'products_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
