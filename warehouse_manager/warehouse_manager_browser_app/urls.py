from django.urls import path
from .views import ProductListView, ProductCreateView, LocalizationCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView
from .views import CategoryCreateView, CategoryListView

urlpatterns = [
    path('product/list', ProductListView.as_view(), name = 'product_list'),
    path('product/create', ProductCreateView.as_view(), name = 'product_create'),
    path('product/detail/<slug:pk>', ProductDetailView.as_view(), name = 'product_detail'),
    path('product/update/<slug:pk>', ProductUpdateView.as_view(), name = 'product_update'),
    path('product/delete/<slug:pk>', ProductDeleteView.as_view(), name = 'product_delete'),
    path('category/list', CategoryListView.as_view(), name = 'category_list'),
    path('category/create', CategoryCreateView.as_view(), name = 'category_create'),
    path('localization/create', LocalizationCreateView.as_view(), name = 'localization_create'),
]