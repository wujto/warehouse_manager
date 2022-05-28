from django.urls import path, include
from .views import ProfileView, UsersListView, WarehouseListView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', ProfileView.as_view(), name = 'profile'),
    path('users', UsersListView.as_view(), name = 'users'),
    path('warehouse', WarehouseListView.as_view(), name = 'warehouse')
]