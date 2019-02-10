from django.shortcuts import render
from rest_framework.generics import ListAPIView
from shipments.models import Shipments
from shipments.serializers import ShipmentsSerializer


class ShipmentsAPIView(ListAPIView):
    queryset = Shipments.objects.all()
    serializer_class = ShipmentsSerializer
