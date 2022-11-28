from django.contrib import admin
from .models import ProductImage,Product,Cart,CartProduct,Order


class ProductImageAdmin(admin.StackedInline):
    model =ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category' , 'selling_price']
    inlines = [ProductImageAdmin]
    
    
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['customer','total']
    
@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ['cart','product','rate','quantity','subtotal']
    
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['cart','subtotal']