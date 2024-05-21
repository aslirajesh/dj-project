# Invoice Items
# Id: UUID
# itemName: string
# Quantity: decimal
# Price: decimal
# Amount: decimal

# Validations for InvoiceItems:
# Amount = Quantity x Price
# Price, Quantity, and Amount must be greater than zero.

import uuid

from django.db import models

from invoice.models.invoice import Invoice


class InvoiceItems(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), editable=False, primary_key=True)
    invoice = models.ForeignKey(Invoice, related_name="items", on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    quantity = models.DecimalField(decimal_places=2, max_digits=10)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    amount = models.DecimalField(decimal_places=2, max_digits=10)

    def save(self, *args, **kwargs):
        self.amount = self.quantity * self.price
        if self.quantity <=0 or self.price <= 0 or self.amount <=0:
            raise ValueError("Price, Quantity, and Amount must be greater than zero")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.item_name

