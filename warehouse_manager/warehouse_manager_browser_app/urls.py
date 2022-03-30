from django.urls import path, include
from .views import ProfileView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', ProfileView.as_view(), name = 'profile')
]