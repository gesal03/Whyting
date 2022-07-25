from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    id= models.AutoField(primary_key=True, verbose_name='Primary Key')
    name = models.CharField(max_length=30, verbose_name='가게 이름')
    introduction = models.TextField(verbose_name='가게 설명')
    address = models.CharField(max_length=30, verbose_name='가게 주소')
    number = models.CharField(max_length=30, verbose_name='가게 전화번호')
    waiting_state = models.IntegerField(default=1)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    start_time=models.IntegerField(null=True)
    end_time=models.IntegerField(null=True)
    def __str__(self):
        return self.name

class Seat(models.Model):
    id=models.AutoField(primary_key=True, verbose_name='Primary Key')
    people=models.IntegerField
    description=models.CharField(max_length=100, verbose_name='좌석 정보')
    name=models.CharField(max_length=30, verbose_name='카테고리 이름')
    store_id=models.ForeignKey(Store, on_delete=models.CASCADE, related_name='seat_store')

class SeatImage(models.Model):
    seat_id=models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='seat_image')
    image = models.ImageField(blank=True, null=True, upload_to = 'store_image')

class Time(models.Model):
    time=models.IntegerField
    store_id=models.ForeignKey(Store, on_delete=models.CASCADE, related_name='time_store')

class Image(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_image')
    image = models.ImageField(blank=True, null=True, upload_to = 'store_image')
