from rest_framework import serializers

from warehouse_manager_base.models import LocalizationModel, CustomUserModel

class LocalizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocalizationModel
        fields = '__all__'
    

class CustomeUserModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = '__all__'