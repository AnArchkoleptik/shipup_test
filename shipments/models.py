from django.db import models


class Shipments(models.Model):
    name = models.CharField(max_length=200)
    company_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    international_transportation_mode = models.CharField(max_length=200)
    international_departure_date = models.DateField()

    class Meta:
        db_table = 'shipments'
