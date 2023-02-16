from django.urls import include, path
from rest_framework import routers

from users.views import LocalizationViewset, ProfileViewset

router = routers.DefaultRouter()
router.register('localizations', LocalizationViewset)
router.register('users', ProfileViewset)

urlpatterns = [
    path('', include(router.urls)),
]