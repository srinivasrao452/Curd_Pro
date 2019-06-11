from rest_framework import viewsets
from Curd_App.models import ProductData
from Curd_App.api.serializers import ProductData_Serializer

class ProductDataView(viewsets.ModelViewSet):
    queryset = ProductData.objects.all()
    serializer_class = ProductData_Serializer

