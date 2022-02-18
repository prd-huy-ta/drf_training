from rest_framework import serializers

from .invoice_item import InvoiceItemSerializer
from ..models import Invoice, InvoiceItem
from datetime import datetime


class InvoiceSerializer(serializers.ModelSerializer):
    invoice_item_names = serializers.StringRelatedField(
        source='invoice_items',
        many=True,
        read_only=True
    )
    invoice_items = InvoiceItemSerializer(many=True, write_only=True)
    customer_name = serializers.StringRelatedField(source='customer', read_only=True)

    class Meta:
        model = Invoice
        fields = ['id', 'customer', 'customer_name', 'total', 'invoice_item_names', 'invoice_items']

    def validate(self, attrs):
        print('attrs:', attrs)
        customer = attrs.get('customer', '')
        invoice_items = attrs.get('invoice_items', [])

        if not customer:
            raise serializers.ValidationError('Customer must exist!')
        if not len(invoice_items):
            raise serializers.ValidationError('Invoice Items must not be empty!')

        validated_data = {}
        validated_data.update(attrs)

        return validated_data

    def create(self, validated_data):
        invoice_items = validated_data.pop('invoice_items')
        validated_data.update(
            {'created_date': datetime.now(),
             'updated_date': datetime.now(),
             'total': sum(
                 [invoice_item['quantity'] * invoice_item['product'].price for invoice_item in invoice_items])}
        )
        invoice = Invoice.objects.create(**validated_data)

        for invoice_item in invoice_items:
            invoice_item.update(
                {'created_date': datetime.now(),
                 'updated_date': datetime.now()}
            )
            InvoiceItem.objects.create(invoice=invoice, **invoice_item)
        return invoice

    def update(self, instance, validated_data):
        invoice_items = validated_data.pop('invoice_items')
        validated_data.update(
            {
                'id': instance.id,
                'created_date': datetime.now(),
                'updated_date': datetime.now(),
                'total': sum(
                    [invoice_item['quantity'] * invoice_item['product'].price for invoice_item in invoice_items])
            }
        )
        invoice = Invoice.objects.update_or_create(**validated_data)

        for invoice_item in invoice_items:
            invoice_item.update(
                {'id': instance.id,
                 'created_date': datetime.now(),
                 'updated_date': datetime.now()}
            )
            InvoiceItem.objects.update_or_create(invoice=invoice, **invoice_item)

        return invoice
