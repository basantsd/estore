from django.shortcuts import render
from django.views import View
from .models import Product
from shop.models import Category,Brand,Color


class ShopView(View):
    template_name = "shop.html"
    def get(self,request,*args,**kwargs):
        context = {}
        category_list = Category.objects.filter(is_active=True)
        context['category_list'] = category_list
        brand_list = Brand.objects.filter(is_active=True)
        context['brand_list'] = brand_list
        color_list = Color.objects.filter(is_active=True)
        context['color_list'] = color_list
        if request.GET:
            print(request.GET)
        else:
            products = Product.objects.filter(is_active=True)
            context['product_list'] = products
        return render(request,self.template_name,context)

class ShopDetailView(View):
    template_name = "shop-details.html"
    def get(self,request,*args,**kwargs):
        pslug =  kwargs['pd']
        pdetail = Product.objects.get(slug=pslug)
        context = { 'product' : pdetail }
        return render(request,self.template_name,context)
        
    
    
class CartView(View):
    template_name = "cart.html"
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    
class CheckoutView(View):
    template_name = "checkout.html"
    def get(self,request,*args,**kwagrs):
        return render(request, self.template_name)
    
    
class AjaxView(View):
    pass

