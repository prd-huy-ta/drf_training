from .base_model import BaseModel
from django.db import models
from django.db.models import fields


class Inventory(BaseModel):
    product = models.OneToOneField('Product', on_delete=models.CASCADE, )
    quantity = fields.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} {self.product.unit} of {self.product}"
