from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from warehouse_manager_base.models import ProductModel, CategoryModel, LocalizationModel, ConfirmationOfTransfer, CustomUserModel

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'logged_in/base.html'

class UsersListView(LoginRequiredMixin, ListView):
    model = CustomUserModel
    template_name = 'logged_in/users_list.html'

class WarehouseListView(LoginRequiredMixin, ListView):
    queryset = ProductModel.objects.filter(localization = 1)
    template_name = 'logged_in/warehouse_list.html'