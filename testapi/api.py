from rest_framework import viewsets, permissions
from .serializers import *


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = CustomerSerializer
