# Invoice Header
# Id: UUID
# Date: string (UTC)
# InvoiceNumber: number
# CustomerName: string
# BillingAddress: string
# ShippingAddress: string
# GSTIN: string
# TotalAmount: Decimal
# Validations for Invoice:
# TotalAmount = Sum(InvoiceItems’s Amount) + Sum(InvoiceBillSundry’s Amount)
# InvoiceNumber should autoincremental and hence should be unique.


import uuid
from django.db import models


class Invoice(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), editable=False,)
    date = models.DateTimeField()
    invoice_number = models.AutoField(unique=True, primary_key=True)
    customer_name = models.CharField(max_length=100)
    billing_address = models.TextField()
    shipping_address = models.TextField()
    gstin = models.CharField(max_length=20)
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)

    def save(self, *args, **kwargs):
        total_item_amount = sum(item.amount for item in self.items.all())
        total_bill_sundry_amount = sum(bill.amount for bill in self.billsundrys.all())
        self.total_amount = total_item_amount + total_bill_sundry_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return f"invoice {self.invoice_number}, {self.customer_name}"
