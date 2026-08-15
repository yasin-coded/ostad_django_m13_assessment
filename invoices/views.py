from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Invoice
from .serializers import InvoiceSerializer
from inventory.permissions import IsStaffOrAdminOrReadOnly


from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum, Count, F
from .models import Invoice, InvoiceItem



# Create your views here.
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsStaffOrAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class InvoiceReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        total_invoices = Invoice.objects.count()

        total_sales = InvoiceItem.objects.aggregate(
            total=Sum(F('quantity') * F('price'))
        )['total'] or 0

        total_products_sold = InvoiceItem.objects.aggregate(
            total=Sum('quantity')
        )['total'] or 0

        return Response({
            'total_invoices': total_invoices,
            'total_sales': total_sales,
            'total_products_sold': total_products_sold,
        })


