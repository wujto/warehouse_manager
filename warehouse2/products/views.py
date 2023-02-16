from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions

from products.models import Product
from products.serializers import ProductSerializer

class HasPermissionOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if not request.method in permissions.SAFE_METHODS:
                if request.user.is_admin:
                    return True
                return False
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if request.user == obj.responsible_person or request.user.is_admin:
                return True
            return False

class ProductListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    pagination_class = ProductListPagination
    serializer_class = ProductSerializer
    permission_classes = [HasPermissionOrReadOnly,]

