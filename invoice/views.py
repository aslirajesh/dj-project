from rest_framework import viewsets

from invoice.models import Invoice
from invoice.serializers import InvoiceSerializers


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializers
