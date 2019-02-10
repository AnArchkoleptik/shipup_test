from django.db import models


class ShipmentProducts(models.Model):
    product_id = models.IntegerField()
    shipment_id = models.IntegerField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'shipment_products'
