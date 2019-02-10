from django.db import models


class Products(models.Model):
    sku = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    company_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = 'products'
