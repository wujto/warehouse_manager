from django.urls import path, include
from .views import ProfileView, UsersListView, WarehouseListView, ProductDetailsView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', ProfileView.as_view(), name = 'profile'),
    path('product/<pk>',ProductDetailsView.as_view(), name = 'product_detail'),
    path('users', UsersListView.as_view(), name = 'users'),
    path('warehouse', WarehouseListView.as_view(), name = 'warehouse')
]