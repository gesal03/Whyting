from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=13, verbose_name='전화번호')
    name = models.CharField(max_length=10,  verbose_name='이름')
    # 0 == owner , 1 == customer
    belong = models.IntegerField()

