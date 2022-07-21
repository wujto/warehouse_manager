from django.urls import path, include
from rest_framework import routers
from .views import LocalizationListViewset, UserListView, ProductViewset, CategoryViewset, ConfirmationOfTransferViewset
from .views import login

router = routers.DefaultRouter()
router.register( r'localizations', LocalizationListViewset )
router.register(r'users', UserListView)
router.register(r'products', ProductViewset)
router.register(r'category', CategoryViewset)
router.register(r'confirmation-of-transfers', ConfirmationOfTransferViewset)
urlpatterns = [
    path( '', include(router.urls) ),
    path('login/', login)
]
