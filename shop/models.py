from django.db import models
from core.base.models import BaseModel
from colorfield.fields import ColorField
from tinymce.models import HTMLField


class Brand(BaseModel):
    title = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True)
    image =  models.ImageField(upload_to="brand",help_text="best size: 440x440px")
    is_active = models.BooleanField(default=True,help_text="Check this for 'Active'")
    
    def __str__(self):
        return self.title


class Category(BaseModel):
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(unique=True)
    subtitle = models.CharField(max_length=200,null=True,blank=True)
    image =  models.ImageField(upload_to="category",help_text="best size: 440x440px")
    is_active = models.BooleanField(default=True,help_text="Check this for 'Active'")
    
    def __str__(self):
        return self.title



class Color(BaseModel):
    color_name = models.CharField(max_length=100,unique=True)
    color_select = ColorField(unique=True)
    is_active = models.BooleanField(default=True,help_text="Check this for 'Active'")

    def __str__(self) -> str:
        return self.color_name



class Size(BaseModel):
    size_name = models.CharField(max_length=100)
    size_detail = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True,help_text="Check this for 'Active'")
    
    def __str__(self) -> str:
        return self.size_name
