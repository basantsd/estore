from django.db import models
from core.base.models import BaseModel
from colorfield.fields import ColorField
from tinymce.models import HTMLField
from django.utils.text import slugify

class Brand(BaseModel):
    title = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    image =  models.ImageField(upload_to="brand",help_text="best size: 440x440px")
    is_active = models.BooleanField(default=True,help_text="Check this for 'Active'")
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Brand, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title


class Category(BaseModel):
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(unique=True,null=True,blank=True)
    subtitle = models.CharField(max_length=200,null=True,blank=True)
    image =  models.ImageField(upload_to="category",help_text="best size: 440x440px")
    is_active = models.BooleanField(default=True,help_text="Check this for 'Active'")
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
    
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


class ContactUs(BaseModel):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Contact-Us"
        verbose_name_plural = "Contact-Us"
        