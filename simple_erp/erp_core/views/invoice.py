from django.db.models import Q
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..serializers import InvoiceSerializer
from ..models import Invoice


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Invoice.objects.all()

        filter_params = self.build_filter(self.request.query_params)
        return queryset.filter(filter_params).order_by('id')

    @staticmethod
    def build_filter(query_params):
        filter_params = ~Q(pk__in=[])

        customer = query_params.get('customer', None)

        if customer is not None:
            filter_params &= Q(first_name__contains=customer)

        return filter_params
