from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from warehouse_manager_base.models import ProductModel, CategoryModel, LocalizationModel, ProductSetModel, ConfirmationOfTransfer, CustomUserModel

class ProfileView(TemplateView):
    template_name = 'logged_in/base.html'