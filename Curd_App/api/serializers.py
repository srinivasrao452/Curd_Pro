from rest_framework import serializers
from Curd_App.models import ProductData

class ProductData_Serializer(serializers.ModelSerializer):
    class Meta:
        model = ProductData
        fields = '__all__'