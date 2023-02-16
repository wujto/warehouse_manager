from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views import ProductViewset

router = DefaultRouter()
router.register('', ProductViewset)

urlpatterns = [
    path('', include(router.urls)),
]