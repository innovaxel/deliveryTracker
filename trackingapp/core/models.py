from django.db import models
from django.utils import timezone

# Create your models here.


class OrderTrack(models.Model):
    """
    This class represents the order tracking model
    """
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField(default=timezone.now())
    sender_name = models.CharField(max_length=100)
    sender_address = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    receiver_address = models.CharField(max_length=100)
    receiver_email = models.EmailField()
    receiver_phone = models.CharField(max_length=10)
    tracking_id = models.CharField(max_length=100)

    def __str__(self):
        return str(self.order_id)
