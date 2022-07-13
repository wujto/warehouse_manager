from django.urls import path, include
from rest_framework import routers
from .views import LocalizationListViewset, UserProfileViewset

router = routers.DefaultRouter()
router.register( r'localizations', LocalizationListViewset )
router.register(r'profile', UserProfileViewset)
urlpatterns = [
    path( '', include(router.urls) ),
]
