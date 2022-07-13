from django.shortcuts import render
from rest_framework import viewsets 

from warehouse_manager_base.models import LocalizationModel, CustomUserModel
from .serializers import LocalizationSerializer, CustomeUserModelSerializer

class LocalizationListViewset(viewsets.ModelViewSet):
    queryset = LocalizationModel.objects.all()
    serializer_class = LocalizationSerializer


class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class = CustomeUserModelSerializer
    queryset = CustomUserModel.objects.get_queryset()
    
    def get_queryset(self):
        user = CustomUserModel.objects.filter(pk = self.request.user.pk)
        if user is not None:
            return user
        else:
            pass