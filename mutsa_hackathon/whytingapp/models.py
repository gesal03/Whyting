from django.db import models
from accounts.models import Owner

class Store(models.Model):
    id= models.AutoField(primary_key=True, verbose_name='Primary Key')
    name = models.CharField(max_length=30, verbose_name='가게 이름')
    introduction = models.TextField(verbose_name='가게 설명')
    address = models.CharField(max_length=30, verbose_name='가게 주소')
    number = models.CharField(max_length=30, verbose_name='가게 전화번호')
    waiting_state = models.IntegerField(default='1')
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='owner')
    """
    store_time
    store_seat
    """
    def __str__(self):
        return self.name

class Image(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(blank=True, null=True, upload_to = 'stroe_image')
