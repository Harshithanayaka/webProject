from rest_framework import viewsets

from offers import serializers
from offers.models import userdetails
from offers.models import Customer

class UserdetailsViewSet(viewsets.ModelViewSet):
    queryset = userdetails.objects.all()
    serializer_class = serializers.userdetailsSerializer

class CustomerDetailsViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerDetailsSerializer