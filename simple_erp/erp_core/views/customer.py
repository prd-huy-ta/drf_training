from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import CustomerSerializer
from ..models import Customer


class CustomerViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request, *args, **kwargs):

        queryset = Customer.objects.all()
        filters = self.build_filter(kwargs)

        customer = self.filter_queryset(queryset.filter(filters).order_by('id'))

        page = self.paginate_queryset(customer)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(page, many=True)
        result_set = serializer.data

        return Response(result_set)

    @staticmethod
    def build_filter(query_params):
        filter_params = ~Q(pk__in=[])

        first_name = query_params.get('first_name')
        last_name = query_params.get('last_name')
        phone = query_params.get('phone')

        if first_name is not None:
            filter_params &= Q(first_name__contains=first_name)
        if last_name is not None:
            filter_params &= Q(first_name__contains=last_name)
        if phone is not None:
            filter_params &= Q(phone__contains=phone)

        return filter_params
