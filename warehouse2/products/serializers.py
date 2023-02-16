from rest_framework import serializers

from products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','id_number', 'name', 'description', 'responsible_person', 'transfer_person', 'photo', 'add_date_time', 'last_modified']
