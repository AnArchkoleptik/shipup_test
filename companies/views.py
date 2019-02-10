from django.shortcuts import render
from rest_framework.generics import ListAPIView
from companies.models import Companies
from companies.serializers import CompaniesSerializer


class CompaniesAPIView(ListAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
