from .base_model import BaseModel
from django.db.models import fields


class Unit(BaseModel):
    name = fields.CharField(max_length=10)
    description = fields.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
