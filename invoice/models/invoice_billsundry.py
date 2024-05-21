# Id: UUID
# billSundryName: string
# Amount: decimal
# #
import uuid

from django.db import models

from invoice.models.invoice import Invoice


class InvoiceBillSundry(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), editable=False,
                          primary_key=True)
    invoice = models.ForeignKey(Invoice, related_name="billsundrys",
                                on_delete=models.CASCADE)
    bill_sundry_name = models.CharField(max_length=100)
    amount = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.bill_sundry_name
