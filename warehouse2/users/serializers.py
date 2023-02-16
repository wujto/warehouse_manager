from rest_framework.serializers import ModelSerializer
from users.models import Profile, Localization

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'phone_number', 'localization', 'photo', 'products', 'transfers']


class LocalizationSerializer(ModelSerializer):
    class Meta:
        model = Localization
        fields = ['name']