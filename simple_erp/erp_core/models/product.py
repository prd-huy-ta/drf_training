from .base_model import BaseModel
from django.db.models import fields
from django.db import models


class Product(BaseModel):
    name = fields.CharField(max_length=30)
    description = fields.CharField(max_length=200)
    price = fields.PositiveIntegerField()
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
