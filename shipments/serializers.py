from rest_framework import serializers
from shipments.models import Shipments 


class ShipmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipments
        fields = (
            'name',
            'company_id',
            'international_transportation_mode',
            'international_departure_date',
        )