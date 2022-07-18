from tokenize import Token
from django.contrib.auth import authenticate
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
    return Response({'token': token.key},
                    status=HTTP_200_OK)



class ProfileViewset(viewsets.ModelViewSet):
    queryset = CustomUserModel.objects.all()
    serializer_class = CustomeUserModelSerializer

    def get_queryset(self):
        profile = CustomUserModel.objects.filter(pk = self.request.user.id).first()
        return profile


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