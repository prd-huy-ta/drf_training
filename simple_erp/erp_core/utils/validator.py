from rest_framework import serializers


class HasLength:
    def __init__(self, base, field):
        self.instance = None
        self.base = base
        self.field = field

    def __call__(self, attrs):
        if len(attrs[self.field]) != self.base:
            message = f'Field {self.field}\'s size must be a of {self.base} characters.'
            raise serializers.ValidationError(message)


def must_be_alphabetic(value):
    if not value.isalpha():
        raise serializers.ValidationError(f'{value} must be alphabetic')
