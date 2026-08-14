from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Invoice
from .serializers import InvoiceSerializer


# Create your views here.
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

