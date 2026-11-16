from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class profile(models.Model):
    ROLE_CHOICES=(
        ('CUSTOMER','customer'),
        ('DRIVER','driver'),
    )
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    role=models.CharField(max_length=20,choices=ROLE_CHOICES)

class Ride(models.Model):
    STATUS_CHOICES=(
        ('REQUESTED','requested'),
        ('ACCEPTED','accepted'),
        ('STARTED','started'),
        ('COMPLETED','completed'),
        ('CANCELLED','cancelled'),
    )
    customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='customer_rides')
    driver=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='driver_rides')
    pickup_location=models.CharField(max_length=50)
    drop_location=models.CharField(max_length=50)
    fare=models.DecimalField(max_digits=4,decimal_places=2,default=0)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='REQUESTED')
    create_at=models.DateTimeField(auto_now_add=True)


