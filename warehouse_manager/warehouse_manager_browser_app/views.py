from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from warehouse_manager_base.models import ProductModel, CategoryModel, LocalizationModel, ConfirmationOfTransfer, CustomUserModel

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'logged_in/profile.html'

class UsersListView(LoginRequiredMixin, TemplateView):
    template_name = 'logged_in/users_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['object_list'] = CustomUserModel.objects.all()
        return context

class WarehouseListView(LoginRequiredMixin, ListView):
    queryset = ProductModel.objects.filter(localization = 1)
    template_name = 'logged_in/warehouse_list.html'

class ProductDetailsView(LoginRequiredMixin, DetailView):
    model = ProductModel
    template_name = 'logged_in/details.html'

class TransferFormView(LoginRequiredMixin, CreateView):
    model = ConfirmationOfTransfer
    template_name = 'logged_in/transfer.html'
    fields = ['product', 'owner','recipient']
    success_url = '/'

    def get_initial(self):
        initial = {}
        initial['product'] = ProductModel.objects.filter(pk = self.kwargs['pk']).first()
        
        if not initial['product'].product_user:
            initial['owner'] = CustomUserModel.objects.get(pk=self.request.user.id)
        else:
            initial['owner'] = initial['product'].product_user

        initial['recipient'] = CustomUserModel.objects.get(pk=self.request.user.id)
        return initial

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['product'] = ProductModel.objects.filter(pk = self.kwargs['pk']).first()
        return context


def confirm_transfer(request, *args, **kwargs):
    confirmation = ConfirmationOfTransfer.objects.filter(pk = kwargs['pk']).first()
    product = confirmation.product
    product.product_user = confirmation.recipient
    product.localization = confirmation.recipient.localization
    product.save()
    confirmation.delete()
    return redirect('profile')

def reject_transfer(request, *args, **kwargs):
    confirmation = ConfirmationOfTransfer.objects.filter(pk = kwargs['pk']).first()
    confirmation.delete()
    return redirect('profile')

class ProductCreateView(LoginRequiredMixin, CreateView):
    model= ProductModel
    fields = '__all__'
    success_url = '/warehouse'
    template_name = 'admin/create_product.html'

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(*args, **kwargs)
        initial['localization'] = LocalizationModel.objects.filter(pk=1).first()
        return initial

class CreateNewCategoryView(LoginRequiredMixin, CreateView):
    model = CategoryModel
    fields = '__all__'
    success_url = '/warehouse/add-product'
    template_name = 'admin/base_form.html'

class CreateCustomeUser(LoginRequiredMixin, CreateView):
    model = CustomUserModel
    fields = '__all__'
    success_url = '/users'
    template_name = 'admin/base_form.html'