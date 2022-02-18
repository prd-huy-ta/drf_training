from .base_model import BaseModel
from django.db.models import fields


class Customer(BaseModel):
    first_name = fields.CharField(max_length=20)
    last_name = fields.CharField(max_length=20)
    date_of_birth = fields.DateField()
    phone = fields.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
