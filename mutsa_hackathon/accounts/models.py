from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id= models.AutoField(primary_key=True, verbose_name='Primary Key')
    number = models.CharField(max_length=13, verbose_name='전화번호')
    name = models.CharField(max_length=10,  verbose_name='이름')
    # 0 == owner , 1 == customer
    belong = models.IntegerField()
    
    def __str__(self):
        return self.user.username


class Owner(models.Model):
    owner_id = models.AutoField(primary_key = True, verbose_name='Primary Key')
    id = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True, verbose_name='Primary Key')
    id = models.ForeignKey(Profile, on_delete=models.CASCADE)

