from django.db import models
from django.contrib.auth.models import User, Group
from .constaint import USER_ROLE,NATIONALITY,STATUS_BLOOD

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=10,choices=USER_ROLE,default='student')
    phone = models.CharField(max_length=14,unique=True)
    email = models.CharField(max_length=50,unique=True)
    
    roll = models.CharField(max_length=8,unique=True,null=True,blank=True)
    registration = models.CharField(max_length=40,unique=True,null=True,blank=True)
    department = models.CharField(max_length=12,null=True,blank=True)
    session = models.CharField(max_length=4,null=True,blank=True)
    address = models.CharField(max_length=100)
    blood = models.CharField(choices=STATUS_BLOOD,max_length=10,null=True,blank=True)

    nationality_type = models.CharField(max_length=10,choices=NATIONALITY)
    nationality_number = models.CharField(max_length=17,unique=True)

    def __str__(self):
        return f"{self.roll} - {self.session}"



