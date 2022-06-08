from django.urls import path, include
from .views import ProfileView, UsersListView, WarehouseListView, ProductDetailsView, TransferFormView, ProductCreateView
from .views import CreateNewCategoryView, CreateCustomeUser, DeleteCustomeUser, UpdateCustomeUser, UserDetailView,UpdateUserPermissionView

from .views import confirm_transfer, reject_transfer

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', ProfileView.as_view(), name = 'profile'),
    path('product/<pk>',ProductDetailsView.as_view(), name = 'product_detail'),
    path('transfer/<pk>', TransferFormView.as_view(), name = 'transfer'),
    path('transfer/confirm/<pk>', confirm_transfer, name = 'transfer_confirm'),
    path('transfer/reject/<pk>', reject_transfer, name= 'transfer_reject'),
    path('users', UsersListView.as_view(), name = 'users'),
    path('warehouse', WarehouseListView.as_view(), name = 'warehouse'),
    path('warehouse/add-product', ProductCreateView.as_view(), name = 'add_product'),
    path('warehouse/add-product/new-category', CreateNewCategoryView.as_view(),name='new_category'),
    path('users/new', CreateCustomeUser.as_view(), name = 'new_user'),
    path('user/<pk>', UserDetailView.as_view(), name='user_detail'),
    path('user/<pk>/permissions', UpdateUserPermissionView.as_view(), name = 'change_permissions'),
    path('user/<pk>/delete', DeleteCustomeUser.as_view(), name = 'delete_user'),
    path('settings/<pk>', UpdateCustomeUser.as_view(), name = 'settings'),
]