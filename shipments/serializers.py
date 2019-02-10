from rest_framework import serializers
from shipments.models import Shipments 


class ShipmentsSerializer(serializers.ModelSerializer):
    international_departure_date = serializers.DateField()

    class Meta:
        model = Shipments
        fields = (
            'id',
            'name',
            'company_id',
            'international_transportation_mode',
            'international_departure_date',
        )