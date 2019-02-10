from django.shortcuts import render
from rest_framework.generics import ListAPIView
from products.models import Products
from products.serializers import ProductsSerializer


class ProductsAPIView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
