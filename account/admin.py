from django.contrib import admin
from .models import Customer,CustomerAddress
from core.base.admin import BaseAdmin
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(BaseAdmin):
    list_display = ['mobile_no','is_email_verfiled','is_active']
    
@admin.register(CustomerAddress)
class CustomerAddressAdmin(BaseAdmin):
    list_display = ['address_type','street_address','city','state','postal_code','country','default','is_active']