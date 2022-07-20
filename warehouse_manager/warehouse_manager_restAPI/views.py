from http.client import HTTPResponse
from tokenize import Token
from urllib.request import Request
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework import viewsets 
from warehouse_manager_base.models import LocalizationModel, CustomUserModel, ProductModel, CategoryModel, ConfirmationOfTransfer
from .serializers import LocalizationSerializer, CustomeUserModelSerializer, ProductSerializer, CategorySerializer
from .serializers import  ConfirmationOfTransferSerializer


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'Token': token.key},
                    status=HTTP_200_OK)


class ProfileViewset(viewsets.ModelViewSet):
    queryset = CustomUserModel.objects.all()
    serializer_class = CustomeUserModelSerializer

    def get_queryset(self):
        profile = CustomUserModel.objects.filter(pk = self.request.user.id)
        return profile


class LocalizationListViewset(viewsets.ModelViewSet):
    queryset = LocalizationModel.objects.all()
    serializer_class = LocalizationSerializer


class UserListView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CustomeUserModelSerializer
    queryset = CustomUserModel.objects.all()


class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()


class ConfirmationOfTransferViewset(viewsets.ModelViewSet):
    serializer_class = ConfirmationOfTransferSerializer
    queryset = ConfirmationOfTransfer.objects.all()

    def create(self, request, *args, **kwargs):
        owner = request.user
        recipient = CustomUserModel.objects.filter(id = request.data['recipient']).first()
        product = ProductModel.objects.filter(id = request.data['product']).first()
        instance = ConfirmationOfTransfer.objects.create(owner = owner, recipient = recipient, product = product)
        instance.save()
        return HttpResponse(HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        confirmation = self.get_object()
        confirmation.status = confirmation.CHOICES[int(request.data['status'])]
        confirmation.save()
        return HttpResponse(HTTP_200_OK)
