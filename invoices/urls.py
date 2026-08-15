from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, InvoiceReportView
from django.urls import path

router = DefaultRouter()
router.register('invoices', InvoiceViewSet)

urlpatterns = router.urls +[
    path('reports/invoice/', InvoiceReportView.as_view(), name='invoice-report'),
]