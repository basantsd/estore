from django.db import models
from django.contrib.auth.models import User
from core.base.models import BaseModel


class Customer(BaseModel):
    user_id = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile_no = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to='profile/',null=True,blank=True)
    is_email_verfiled = models.BooleanField(default=False)
    token = models.CharField(max_length=100,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.user_id.email
    



ADDRESS_TYPE = (
    ("ship","shipping"),
    ("bill","billing"),
)

class CustomerAddress(BaseModel):
    user_id = models.OneToOneField(User,on_delete=models.PROTECT)
    address_type = models.CharField(max_length=10,choices=ADDRESS_TYPE,default="ship")
    street_address = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    postal_code = models.PositiveIntegerField(null=True,blank=True)
    country = models.CharField(max_length=200,default='India')
    default = models.BooleanField(default=False)
    is_active = models.BooleanField(blank=True)
    
    def __str__(self) -> str:
        return self.postal_code+' '+self.country




