from .base_model import BaseModel
from django.db import models
from django.db.models import fields


class Invoice(BaseModel):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    total = fields.PositiveIntegerField()

    def __str__(self):
        return f"Invoice {self.id}"
