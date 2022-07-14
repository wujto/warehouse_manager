from django.shortcuts import render
from rest_framework import viewsets 

from warehouse_manager_base.models import LocalizationModel, CustomUserModel, ProductModel, CategoryModel, ConfirmationOfTransfer
from .serializers import LocalizationSerializer, CustomeUserModelSerializer, ProductSerializer, CategorySerializer, ConfirmationOfTransferSerializer

class LocalizationListViewset(viewsets.ModelViewSet):
    queryset = LocalizationModel.objects.all()
    serializer_class = LocalizationSerializer


class UserListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CustomeUserModelSerializer
    queryset = CustomUserModel.objects.all()
    # lookup_url_kwarg = 'slug'
    # lookup_localization_kwarg = 'slug'


class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()
    # lookup_product_user_kwarg = 'slug'


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()


class ConfirmationOfTransferViewset(viewsets.ModelViewSet):
    serializer_class = ConfirmationOfTransferSerializer
    queryset = ConfirmationOfTransfer.objects.all()