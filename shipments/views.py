from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from rest_framework.generics import ListAPIView
from shipments.models import Shipments
from shipments.serializers import ShipmentsSerializer


class ShipmentsAPIView(ListAPIView):
    queryset = Shipments.objects.all()
    serializer_class = ShipmentsSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        company_id = self.request.GET.get('company_id', None)
        sort = self.request.GET.get('sort', None)
        direction = self.request.GET.get('direction', None)
        international_transportation_mode = self.request.GET.get('international_transportation_mode', None)
        page = self.request.GET.get('page', None)
        per = self.request.GET.get('per', None)

        if not company_id:
            # return error "company_id needed"
            return qs
        
        qs = Shipments.objects.filter(company_id=company_id)

        if international_transportation_mode:
            qs = qs.filter(international_transportation_mode=international_transportation_mode)
        
        if sort:
            if direction == 'desc':
                qs = qs.order_by(f'-{sort}')
            else:
                qs = qs.order_by(sort)
        else:
            qs = qs.order_by('id')

        if per:
            paginator = Paginator(qs, per)
        else:
            paginator = Paginator(qs, 4)
        
        if page:
            qs = paginator.page(page)
        else:
            qs = paginator.page(1)

        return qs
