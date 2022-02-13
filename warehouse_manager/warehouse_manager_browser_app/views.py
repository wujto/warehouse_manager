from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from warehouse_manager_base.models import ProductModel, CategoryModel, LocalizationModel, ProductSetModel, ConfirmationOfTransfer, CustomUserModel

class ProductListView(ListView):
    model = ProductModel
    template_name = 'list.html'

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

class ProductUpdateView(UpdateView):
    model = ProductModel
    template_name = 'update.html'
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

class CategoryDetailView(DetailView):
    model = CategoryModel
    template_name = 'detail.html'

class CategoryUpdateView(UpdateView):
    model = CategoryModel
    fields = ['name', 'description']
    template_name = 'update.html'

class CategoryDeleteView(DeleteView):
    model = CategoryModel
    success_url = 'category_list'
    template_name = 'delete.html'

class LocalizationCreateView(CreateView):
    model = LocalizationModel
    fields = ['name', 'description']
    template_name = 'create.html'

class LocalizationListView(ListView):
    model = LocalizationModel
    template_name = 'list.html'

class LocalizationDetailView(DetailView):
    model = LocalizationModel
    template_name = 'detail.html'

class LocalizationUpdateView(UpdateView):
    model = LocalizationModel
    template_name = 'update.html'

class LocalizationDeleteView(DeleteView):
    model = LocalizationModel
    template_name = 'delete.html'
    success_url = 'localization_list'

class ProductSetListView(ListView):
    model = ProductSetModel
    template_name = 'list.html'

class ProductSetCreateView(CreateView):
    model = ProductSetModel
    fields = ['id_number', 'name', 'description']
    template_name = 'create.html'

class ProductSetDetailView(DetailView):
    model = ProductSetModel
    template_name = 'detail.html'

class ProductSetUpdateView(UpdateView):
    model = ProductSetModel
    fields = ['name', 'description']
    template_name = 'update.html'

class ProductSetDeleteView(DeleteView):
    model = ProductSetModel
    template_name = 'delete.html'
    success_url = 'product_set_list'

class ConfirmationListView(ListView):
    model = ConfirmationOfTransfer
    template_name = 'list.html'

class ConfirmationCreateView(CreateView):
    model = ConfirmationOfTransfer
    fields = ['product','recipient']
    template_name = 'create.html'

class ConfirmationDetailView(DetailView):
    model = ConfirmationOfTransfer
    template_name = 'detail.html'

class ConfirmationUpdateView(UpdateView):
    model = ConfirmationOfTransfer
    fields = ['product', 'recipient']
    template_name = 'update.html'

class ConfirmationDeleteView(DeleteView):
    model = ConfirmationOfTransfer
    template_name = 'delete.html'
    success_url = '' # do profilu urzytkownika

class UserListView(ListView):
    model = CustomUserModel
    template_name = 'list.html'

class UserCreateView(CreateView):
    model = CustomUserModel
    fields = ['email', 'password', 'first_name', 'last_name', 'phone_number']
    template_name = 'create.html'

    def post(self, request, *args, **kwargs):
        data = {'first_name':request.POST['first_name'],
        'last_name': request.POST['last_name'],
        'phone_number': request.POST['phone_number']}
        u = self.model.objects.create_user(request.POST['email'],request.POST['password'], **data)
        return redirect(reverse_lazy('user_detail', args = [str(u.pk)]))

class UserDetailView(DetailView):
    model = CustomUserModel
    template_name = 'detail.html'

class UserUpdateView(UpdateView):
    model = CustomUserModel
    fields = ['password', 'first_name', 'last_name', 'phone_number', 'is_admin', 'is_manager', 'user_permissions']
    template_name = 'update.html'

class UserDeleteView(DeleteView):
    model = CustomUserModel
    success_url = reverse_lazy('user_list')
    template_name = 'delete.html'