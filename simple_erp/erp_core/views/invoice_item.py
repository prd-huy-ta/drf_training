from django.db.models import Q
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..serializers import InvoiceSerializer
from ..models import InvoiceItem


class InvoiceItemViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceSerializer
