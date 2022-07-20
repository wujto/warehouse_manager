from rest_framework import serializers

from warehouse_manager_base.models import LocalizationModel, CustomUserModel, ProductModel, CategoryModel, ConfirmationOfTransfer


class LocalizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocalizationModel
        fields = '__all__'
    

class CustomeUserModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ('url', 'email', 'first_name', 'last_name', 'phone_number', 'localization','owned_confirmations', 'recipient_confirmations', 'products')
        extra_kwargs = {
            # 'url' : {'view_name': 'customusermodel-detail'},
            'owned_confirmations' : {'view_name': 'confirmationoftransfer-detail'},
            'recipient_confirmations' : {'view_name': 'confirmationoftransfer-detail'},
            'products' : {'view_name': 'productmodel-detail'},
            # 'localization' : {'view_name': 'localizationmodel-detail'}
        }


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('url', 'id_number', 'name', 'description', 'category', 'localization', 'product_user', 'photo')
        extra_kwargs = {
            'category' : {'view_name': 'categorymodel-detail'},
            # 'product_user' : {'view_name': 'customusermodel-detail', 'lookup_field': 'slug'}
        }


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('url', 'name')


class ConfirmationOfTransferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ConfirmationOfTransfer
        fields = ('url', 'product', 'owner', 'recipient', 'status', 'date')
        read_only_fields = ('owner', 'date', 'url')

        def update(self, instance, validated_data):
            instance.status = validated_data.get('status')
            instance.save()
            return instance
