from django.contrib import admin
from .models import Customer,CustomerAddress
from core.base.admin import BaseAdmin
from django.contrib.auth.models import User
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(BaseAdmin):
    list_display = ['user_name','user_email','mobile_no','is_email_verfiled','is_active']
    list_filter = ['is_email_verfiled','is_active']
    def user_email(self, Customer):
        return Customer.user_id.email
    
    def user_name(self, Customer):
        return Customer.user_id.first_name+' '+Customer.user_id.last_name
    
    
    
    
@admin.register(CustomerAddress)
class CustomerAddressAdmin(BaseAdmin):
    list_display = ['address_type','street_address','city','state','postal_code','country','default','is_active']