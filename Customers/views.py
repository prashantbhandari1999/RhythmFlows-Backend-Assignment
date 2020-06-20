# Create your views here.
from rest_framework import viewsets
from url_filter.integrations.drf import DjangoFilterBackend

from Customers.models import Customer
from Customers.serializers import CustomerSerializer


class CustomersViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name']
