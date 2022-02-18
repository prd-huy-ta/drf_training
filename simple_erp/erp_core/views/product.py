from django.db.models import Q
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..serializers import ProductSerializer
from ..models import Product


class ProductViewSet(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        filter_params = self.build_filter(self.request.query_params)
        return queryset.filter(filter_params).order_by('id')

    @staticmethod
    def build_filter(query_params):
        filter_params = ~Q(pk__in=[])

        name = query_params.get('name')

        if name is not None:
            filter_params &= Q(name__contains=name)

        return filter_params
