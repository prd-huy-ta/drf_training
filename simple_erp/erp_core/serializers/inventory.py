from rest_framework import serializers
from ..models import Inventory

from datetime import datetime


class InventorySerializer(serializers.ModelSerializer):
    product_name = serializers.StringRelatedField()

    class Meta:
        model = Inventory
        fields = ['id', 'product', 'product_name', 'quantity']

    def validate(self, attrs):
        product_id = attrs.get('product', '').strip()
        quantity = attrs.get('quantity', '').strip()

        validated_data = {}

        if not product_id:
            raise serializers.ValidationError('Product Id must not be empty!')

        if not quantity:
            raise serializers.ValidationError('Quantity must not be empty!')

        if not quantity.isdigit():
            raise serializers.ValidationError('Price must be of digits!')

        validated_data.update(attrs)

        return validated_data

    def create(self, validated_data):
        validated_data.update(
            {'created_date': datetime.now(),
             'updated_date': datetime.now()}
        )
        customer = Inventory(**validated_data)
        customer.save()
        return customer

    def update(self, instance, validated_data):
        instance.update(validated_data)
        instance['updated_date'] = datetime.now()
        instance.save()
        return instance
