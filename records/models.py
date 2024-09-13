from django.db import models

class Record(models.Model):
    order_id = models.CharField(max_length=50, primary_key=True)  
    destination = models.CharField(max_length=100)
    destination_iata = models.CharField(max_length=10)
    origin = models.CharField(max_length=100)
    origin_iata = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    departure = models.DateField()
    arrival = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(null=True)

    class Meta:
        db_table = 'record'
