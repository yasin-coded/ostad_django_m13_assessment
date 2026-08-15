from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Invoice
from .serializers import InvoiceSerializer
from inventory.permissions import IsStaffOrAdminOrReadOnly


# Create your views here.
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsStaffOrAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

