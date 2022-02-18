from rest_framework import serializers
from ..models import Product
from datetime import datetime


class ProductSerializer(serializers.ModelSerializer):
    unit_name = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'unit', 'unit_name']

    def validate(self, attrs):
        print(attrs)
        name = attrs.get('name', '')
        price = attrs.get('price', '')
        unit = attrs.get('unit', '')

        validated_data = {}

        if not name:
            raise serializers.ValidationError('Name must not be empty!')

        if not price:
            raise serializers.ValidationError('Price must not be empty!')

        if not unit:
            raise serializers.ValidationError('Unit must not be empty!')

        if str is type(price) and not price.isdigit():
            raise serializers.ValidationError('Price must be of digits!')

        validated_data.update(attrs)

        return validated_data

    def create(self, validated_data):
        validated_data.update(
            {'created_date': datetime.now(),
             'updated_date': datetime.now()}
        )
        customer = Product(**validated_data)
        customer.save()
        return customer

    def update(self, instance, validated_data):
        validated_data['updated_date'] = datetime.now()
        validated_data['created_date'] = instance.created_date
        validated_data['name'] = validated_data.get('name', instance.name)
        validated_data['description'] = validated_data.get('description', instance.description)
        validated_data['price'] = validated_data.get('price', instance.price)
        validated_data['unit'] = validated_data.get('unit', instance.unit)

        instance = super(ProductSerializer, self).update(instance, validated_data)
        instance.save()

        return instance
