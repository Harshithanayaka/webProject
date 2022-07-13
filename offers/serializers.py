from rest_framework import serializers
from offers.models import userdetails
from offers.models import Customer

class userdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = userdetails
        fields = '__all__'
class CustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'