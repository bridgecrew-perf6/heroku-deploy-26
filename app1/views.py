from django.shortcuts import render
from rest_framework import viewsets
from app1.models import Product
from app1.Serializers import ProductSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
