from django.urls import path
from .views import ProductListView, ProductCreateView, CategoryCreateView, LocalizationCreateView, ProductDetailView

urlpatterns = [
    path('product/list', ProductListView.as_view(), name = 'product_list'),
    path('product/create', ProductCreateView.as_view(), name = 'product_create'),
    path('product/detail/<slug:pk>', ProductDetailView.as_view(), name = 'product_detail'),
    path('category/create', CategoryCreateView.as_view(), name = 'category_create'),
    path('localization/create', LocalizationCreateView.as_view(), name = 'localization_create'),
]