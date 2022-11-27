from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name = 'home/index.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    
class AboutView(View):
    template_name = 'home/about.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    
class ShopView(View):
    template_name = "shop.html"
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    
class ShopDetailView(View):
    template_name = "product-details.html"
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    
    
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

