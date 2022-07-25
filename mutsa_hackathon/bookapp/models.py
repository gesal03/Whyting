from sqlite3 import Time
from django.db import models
from django.contrib.auth.models import User
from whytingapp.models import Store, Seat, Time

# Create your models here.

class Reservation(models.Model):
    reservation_id=models.AutoField(primary_key=True, verbose_name='Primary Key')
    store_id=models.ForeignKey(Store, on_delete=models.CASCADE, related_name='reservation_store')
    customer_id=models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservation_customer')
    seat_id=models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='reservation_seat')
    time_id=models.ForeignKey(Time, on_delete=models.CASCADE, related_name='reservation_time')
    def __str__(self):
        return self.user.username