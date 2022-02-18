from rest_framework import serializers
from ..models import Customer

from datetime import datetime
import re


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'phone']

    def validate(self, attrs):
        first_name = attrs.get('first_name', '').strip()
        last_name = attrs.get('last_name', '').strip()
        date_of_birth = attrs.get('date_of_birth', '')
        phone = attrs.get('phone', '').strip()

        validated_data = {}

        if not first_name:
            raise serializers.ValidationError('First Name must not be empty!')

        if not last_name:
            raise serializers.ValidationError('Last Name must not be empty!')

        if not date_of_birth:
            raise serializers.ValidationError('Date of Birth must not be empty!')

        if not phone:
            raise serializers.ValidationError('Phone must not be empty!')

        if not phone.isdigit():
            raise serializers.ValidationError('Phone must be of digits!')

        if 10 != len(phone):
            raise serializers.ValidationError('Phone must be be a 10-digits number!')

        validated_data.update(attrs)
        if str is type(date_of_birth):
            validated_data['date_of_birth'] = datetime.strptime(date_of_birth, '%d-%m-%Y').date()

        return validated_data

    def create(self, validated_data):
        validated_data.update(
            {'created_date': datetime.now(),
             'updated_date': datetime.now()}
        )
        customer = Customer(**validated_data)
        customer.save()
        return customer

    def update(self, instance, validated_data):
        validated_data['updated_date'] = datetime.now()
        validated_data['created_date'] = instance.created_date
        validated_data['first_name'] = validated_data.get('first_name', instance.first_name)
        validated_data['last_name'] = validated_data.get('last_name', instance.last_name)
        validated_data['date_of_birth'] = validated_data.get('date_of_birth', instance.date_of_birth)
        validated_data['phone'] = validated_data.get('phone', instance.phone)

        instance = super(CustomerSerializer, self).update(instance, validated_data)
        instance.save()
        return instance
