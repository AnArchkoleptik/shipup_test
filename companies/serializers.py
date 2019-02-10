from rest_framework import serializers
from companies.models import Companies


class CompaniesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Companies
        fields = ('name', )
