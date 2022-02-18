from .base_model import BaseModel
from django.db import models
from django.db.models import fields


class InvoiceItem(BaseModel):
    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE, related_name='invoice_items')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = fields.PositiveIntegerField()

    def __str__(self):
        return f"{self.invoice}: {self.quantity} {self.product}"
