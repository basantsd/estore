from django.shortcuts import render
from django.views import View
from .models import Product


class ShopView(View):
    template_name = "shop.html"
    def get(self,request,*args,**kwargs):
        context = {}
        if request.GET:
            print(request.GET['category'])
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

