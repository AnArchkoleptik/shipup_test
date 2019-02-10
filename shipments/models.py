from django.db import models
from django.http import JsonResponse
from products.models import Products
from products.serializers import ProductsSerializer
from shipment_products.models import ShipmentProducts
from django.core import serializers


class Shipments(models.Model):
    name = models.CharField(max_length=200)
    company_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    international_transportation_mode = models.CharField(max_length=200)
    international_departure_date = models.DateField()

    class Meta:
        db_table = 'shipments'

    @property
    def products(self):
        products = Products.objects.filter(company_id=self.company_id).values('id', 'sku', 'description')
        products_list = []
        for product in products:
            shipment_product = ShipmentProducts.objects.filter(product_id=product['id']).filter(shipment_id=self.id)
            if len(shipment_product) > 0:
                product['quantity'] = shipment_product.values()[0]['quantity']
                products_list.append(product)
        return products_list
