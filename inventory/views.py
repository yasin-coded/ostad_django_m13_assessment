from django.conf.locale import fr
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
