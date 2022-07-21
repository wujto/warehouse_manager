from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from warehouse_manager_base.models import ProductModel, CategoryModel, LocalizationModel, ConfirmationOfTransfer, CustomUserModel
from .forms import UserUpdateForm

class AdminAccessMixin(PermissionRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_admin:
            return redirect('/')

        return super().dispatch(request, *args, **kwargs)

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

class ProductCreateView(AdminAccessMixin, LoginRequiredMixin, CreateView):
    model= ProductModel
    fields = '__all__'
    success_url = '/warehouse'
    template_name = 'admin/create_product.html'

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(*args, **kwargs)
        initial['localization'] = LocalizationModel.objects.filter(pk=1).first()
        initial['product_owner'] = CustomUserModel.objects.filter(pk = 1).first()
        return initial

class CreateNewCategoryView(AdminAccessMixin, LoginRequiredMixin, CreateView):
    model = CategoryModel
    fields = '__all__'
    success_url = '/warehouse/add-product'
    template_name = 'admin/base_form.html'

class CreateCustomeUser(AdminAccessMixin, LoginRequiredMixin, CreateView):
    model = CustomUserModel
    fields = ('first_name', 'last_name','email', 'password', 'phone_number' ,'is_manager', 'is_admin',)
    success_url = '/users'
    template_name = 'admin/base_form.html'

    def form_valid(self, form):
        if self.request.user.is_admin:
            super().form_valid(form)
            self.object.password = form['password'].value()
            self.object.save_password()
        return redirect('users')

class DeleteCustomeUser(AdminAccessMixin, LoginRequiredMixin, DeleteView):
    model = CustomUserModel
    template_name = 'admin/delete_confirm.html'
    success_url = '/users'

class UpdateCustomeUser(FormView, LoginRequiredMixin):
    form_class = UserUpdateForm
    success_url = '/'
    template_name = 'admin/base_form.html'

    def form_valid(self, form):
        if form['old_password'].value() != '' and form['new_password'].value() == form['new_password2'].value():
            if self.request.user.check_password(form['old_password'].value()):
                self.request.user.password = form['new_password'].value()
                self.request.user.save_password()
        if form['phone_number'].value() !='':
            self.request.user.phone_number = form['phone_number'].value()
        
        self.request.user.save()
        return super().form_valid(form)

class UserDetailView(DetailView, LoginRequiredMixin):
    model = CustomUserModel
    template_name = 'logged_in/user_detail.html'

class UpdateUserPermissionView(AdminAccessMixin, UpdateView, LoginRequiredMixin):
    model = CustomUserModel
    template_name = 'admin/base_form.html'
    fields = ('is_admin',)
    success_url = '/users'

