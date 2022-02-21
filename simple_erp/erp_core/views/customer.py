from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from ..serializers import CustomerSerializer
from ..models import Customer
from rest_framework import status


class CustomerViewSet(viewsets.ViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def update(self, request, pk=None):
        try:
            instance = Customer.objects.filter(pk=pk).first()

            response = {
                'message': ''
            }
            if not instance:
                response.update({
                    'message': 'The thing is not found'
                })
                return Response(response, status=status.HTTP_204_NO_CONTENT)
            serializer = CustomerSerializer(instance, data=request.data)

            if not serializer.is_valid():
                response.update({
                    'message': 'The data is not valid'
                })
                return Response(response, status=status.HTTP_204_NO_CONTENT)

            serializer.save()
            response.update({
                'message': 'Data has been successfully updated!',
                'data': serializer.validated_data
            })

            return Response(response, status=status.HTTP_200_OK)

        except Exception as exception:
            raise exception

    @action(detail=False, methods=["GET"], url_path="listall")
    def list_all(self, request):
        try:
            filter_params = self.build_filter(request.query_params)
            queryset = Customer.objects.all().filter(filter_params).order_by('id')
            serializer = CustomerSerializer(queryset, many=True)

            response = {
                'count': len(serializer.data),
                'custom_field': 'custom',
                'data': serializer.data,
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as exception:
            raise exception

    @action(detail=False, methods=["POST"], url_path='create_one')
    def create_one(self, request):
        try:
            serializer = CustomerSerializer(data=request.data)
            response = {
                'message': 'Created Failed',
                'data': []
            }

            if not serializer.is_valid():
                print(serializer.errors)
                response.update({
                    'reason': serializer.errors
                })
                return Response(response, status=status.HTTP_204_NO_CONTENT)
            response.update({
                'message': 'Successfully created data!',
                'data': serializer.validated_data
            })

            serializer.save()

            return Response(response, status=status.HTTP_204_NO_CONTENT)
        except Exception as exception:
            raise exception

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
