from django.db import models
from shop.models import *
from account.models import Customer,CustomerAddress
from core.base.models import BaseModel
from account.models import User
from django.utils.text import slugify


# Create your models here.
class Product(BaseModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    tages = models.CharField(max_length=200, null=True,blank=True)
    marked_price = models.DecimalField(decimal_places=2,max_digits=8)
    selling_price = models.DecimalField(decimal_places=2,max_digits=8)
    color = models.ManyToManyField(Color , blank=True)
    size = models.ManyToManyField(Size , blank=True)
    description = HTMLField()
    specification = HTMLField()
    is_active = models.BooleanField(default=True,help_text="Check this for 'Active'")
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image =  models.ImageField(upload_to="product")
    is_active = models.BooleanField(default=True,help_text="Check this for 'Active'")
    
    
class Cart(BaseModel):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True, blank=True)
    total = models.DecimalField(decimal_places=2,max_digits=8,default=0)
    
    def __str__(self):
        return "Cart: "+str(self.id)
    
class CartProduct(BaseModel):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE, related_name='cartproduct')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product')
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(decimal_places=2,max_digits=8)
    
    def __str__(self):
        return "Cart: "+str(self.cart.id)+" CartProduct: "+ str(self.id)
    
ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Canceled", "Order Canceled"),
)

class Order(BaseModel):
    cart = models.OneToOneField(Cart,on_delete=models.CASCADE)
    ordered_by = models.ForeignKey(User,on_delete=models.CASCADE,max_length=200)
    mobile = models.CharField(max_length=10)
    shipping_address = models.ForeignKey(CustomerAddress,limit_choices_to={'address_type':'ship'},on_delete=models.PROTECT, related_name="pship",null=True,blank=True)
    billing_address = models.ForeignKey(CustomerAddress,limit_choices_to={'address_type':'bill'},on_delete=models.PROTECT, related_name="pbill",null=True,blank=True)
    subtotal = models.DecimalField(decimal_places=2,max_digits=8,default=0)
    discount = models.DecimalField(decimal_places=2,max_digits=8)
    total = models.DecimalField(decimal_places=2,max_digits=8)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS)
    
    def __str__(self):
        return "Order : "+str(self.id)
    