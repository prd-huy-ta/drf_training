from rest_framework import serializers
from ..models import InvoiceItem, Product


class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ['id', 'product', 'quantity']
