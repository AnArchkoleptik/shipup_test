from rest_framework import serializers
from shipments.models import Shipments 


class ShipmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipments
        fields = (
            'id',
            'name',
            'products',
        )
