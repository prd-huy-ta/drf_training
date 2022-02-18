from rest_framework import serializers
from ..models import Unit

from datetime import datetime


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        validated_data.update(
            {'created_date': datetime.now(),
             'updated_date': datetime.now()}
        )
        customer = Unit(**validated_data)
        customer.save()
        return customer

    def update(self, instance, validated_data):
        validated_data['updated_date'] = datetime.now()
        validated_data['name'] = validated_data.get('name', instance.name)
        validated_data['description'] = validated_data.get('description', instance.description)
        instance = super(UnitSerializer, self).update(instance, validated_data)

        instance.save()
        return instance
