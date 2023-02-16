from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from users.serializers import LocalizationSerializer, ProfileSerializer
from users.models import Localization, Profile


class ProfilePaginationClass(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 15

class LocalizationViewset(ModelViewSet):
    queryset = Localization.objects.all()
    serializer_class = LocalizationSerializer


class ProfileViewset(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = ProfilePaginationClass