from django.db import models
from products.models import Product
from core.base.models import BaseModel

# Create your models here.
class HomeBanner(BaseModel):
    maintitle = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    small_description = models.CharField(max_length=300)
    background_image = models.ImageField(upload_to="home_banner", help_text="1920x801 px image for fit background")
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    
    
class BestProduct(BaseModel):
    title = models.CharField(max_length=200)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    tag = models.CharField(max_length=20,default='danger',null=True,blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    
    
class SiteSetting(BaseModel):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logo')
    
    def __str__(self) -> str:
        return self.name