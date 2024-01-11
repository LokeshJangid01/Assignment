from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, InvoiceDetailVIewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoices-details', InvoiceDetailVIewSet)

urlpatterns = [
    path('', include(router.urls)),
]