from itertools import product
from msilib.schema import ServiceInstall
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Categoty
from .serializers import  ProductSerializer
# Create your views here.

class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)


