from django.urls import path, include
from .views import ProfileView, UsersListView, WarehouseListView, ProductDetailsView, TransferFormView
from .views import confirm_transfer, reject_transfer

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', ProfileView.as_view(), name = 'profile'),
    path('product/<pk>',ProductDetailsView.as_view(), name = 'product_detail'),
    path('transfer/<pk>', TransferFormView.as_view(), name = 'transfer'),
    path('transfer/confirm/<pk>', confirm_transfer, name = 'transfer_confirm'),
    path('transfer/reject/<pk>', reject_transfer, name= 'transfer_reject'),
    path('users', UsersListView.as_view(), name = 'users'),
    path('warehouse', WarehouseListView.as_view(), name = 'warehouse')
]