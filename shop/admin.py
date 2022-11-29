from django.contrib import admin
from .models import *
from core.base.admin import BaseAdmin
# Register your models here.


@admin.register(Brand)
class BrandAdmin(BaseAdmin):
    list_display = ['title','is_active']
    model = Brand

@admin.register(Color)
class ColorAdmin(BaseAdmin):
    list_display = ['color_name', 'color_select','is_active']
    model = Color

    
@admin.register(Category)
class CategoryAdmin(BaseAdmin):
    list_display = ['title','subtitle', 'is_active']
    model = Category


@admin.register(Size)
class SizeAdmin(BaseAdmin):
    list_display = ['size_name', 'size_detail' , 'price','is_active']
    model = Size


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email' , 'message','created_at']
    model = ContactUs