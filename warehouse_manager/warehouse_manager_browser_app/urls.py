from django.urls import path
from .views import ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView
from .views import CategoryCreateView, CategoryListView, CategoryUpdateView, CategoryDeleteView, CategoryDetailView
from .views import LocalizationCreateView, LocalizationListView, LocalizationUpdateView, LocalizationDetailView, LocalizationDeleteView
from .views import ProductSetListView, ProductSetCreateView, ProductSetDetailView, ProductSetUpdateView, ProductSetDeleteView
from .views import ConfirmationListView, ConfirmationCreateView, ConfirmationDetailView, ConfirmationUpdateView, ConfirmationDeleteView
from .views import UserListView, UserCreateView, UserDetailView, UserUpdateView, UserDeleteView

urlpatterns = [
# Product
    path('product/list', ProductListView.as_view(), name = 'product_list'),
    path('product/create', ProductCreateView.as_view(), name = 'product_create'),
    path('product/detail/<slug:pk>', ProductDetailView.as_view(), name = 'product_detail'),
    path('product/update/<slug:pk>', ProductUpdateView.as_view(), name = 'product_update'),
    path('product/delete/<slug:pk>', ProductDeleteView.as_view(), name = 'product_delete'),
# Category
    path('category/list', CategoryListView.as_view(), name = 'category_list'),
    path('category/create', CategoryCreateView.as_view(), name = 'category_create'),
    path('category/detail/<slug:pk>', CategoryDetailView.as_view(), name = 'category_detail'),
    path('category/update/<slug:pk>', CategoryUpdateView.as_view(), name = 'category_update'),
    path('category/delete/<slug:pk>', CategoryDeleteView.as_view(), name = 'category_delete'),
# Localization
    path('localization/list', LocalizationListView.as_view(), name = 'localization_list'),
    path('localization/create', LocalizationCreateView.as_view(), name = 'localization_create'),
    path('localization/detail/<slug:pk>', LocalizationDetailView.as_view(), name = 'localization_detail'),
    path('localization/update/<slug:pk>', LocalizationUpdateView.as_view(), name = 'localization_update'),
    path('localization/delete/<slug:pk>', LocalizationDeleteView.as_view(), name = 'localization_delete'),
# ProductSet
    path('product_set/list', ProductSetListView.as_view(), name = 'product_set_list'),
    path('product_set/create', ProductSetCreateView.as_view(), name = 'product_set_create'),
    path('product_set/detail/<slug:pk>', ProductSetDetailView.as_view(), name = 'product_set_detail'),
    path('product_set/update/<slug:pk>', ProductSetUpdateView.as_view(), name = 'product_set_update'),
    path('product_set/delete/<slug:pk>', ProductSetDeleteView.as_view(), name = 'product_set_delete'),
# ConfirmationOfTransfer
    path('confirmation/list', ConfirmationListView.as_view(), name = 'confirmation_list'),
    path('confirmation/create', ConfirmationCreateView.as_view(), name = 'confirmation_create'),
    path('confirmation/detail/<slug:pk>', ConfirmationDetailView.as_view(), name = 'confirmation_detail'),
    path('confirmation/update/<slug:pk>', ConfirmationUpdateView.as_view(), name = 'confirmation_update'),
    path('confirmation/delete/<slug:pk>', ConfirmationDeleteView.as_view(), name = 'confirmation_delete'),
# User
    path('user/list', UserListView.as_view(), name = 'user_list'),
    path('user/create', UserCreateView.as_view(), name = 'user_create'),
    path('user/detail/<slug:pk>', UserDetailView.as_view(), name = 'user_detail'),
    path('user/update/<slug:pk>', UserUpdateView.as_view(), name = 'user_update'),
    path('user/delete/<slug:pk>', UserDeleteView.as_view(), name = 'user_delete'),
]