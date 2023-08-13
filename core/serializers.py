from  rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        #fields='__all__'
        fields=['customer_id', 'last_name', 'first_name']
        read_only_fields = ('first_name' 'last_name', )