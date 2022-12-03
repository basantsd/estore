from django.shortcuts import render, redirect
from django.views import View
from account.models import Customer
from .models import Product,Cart,CartProduct
from shop.models import Category,Brand,Color


class ShopView(View):
    template_name = "shop.html"
    
    def get(self,request,*args,**kwargs):
        context = {}
        category_list = Category.objects.filter(is_active=True)
        brand_list = Brand.objects.filter(is_active=True)
        color_list = Color.objects.filter(is_active=True)
        
        if (request.GET and request.GET.get('q') == "") or not request.GET:
            products = Product.objects.filter(is_active=True)
            context['product_list'] = products
        elif request.GET:
            if request.GET.get('q') is not None:
                products = Product.objects.filter(title__icontains = request.GET.get('q'))
            elif request.GET.get('category') is not None :
                products = Product.objects.filter(category__slug = request.GET['category'])
            elif request.GET.get('brand') is not None:
                products = Product.objects.filter(brand__slug = request.GET['brand'])
            elif request.GET.get('sort') is not None:
                sortp = request.GET.get('sort')
                q = ''
                if sortp == 'l_h':
                    q = 'selling_price'
                elif sortp == 'h_l':
                    q = '-selling_price'
                elif sortp == 'a_z':
                    q = 'title'
                else:
                    q = '-title'
                
                products = Product.objects.all().order_by(q)
            elif request.GET.get('color') is not None:
                products = Product.objects.filter(color__color_name = request.GET['color'])
            elif request.GET.get('srate') is not None and request.GET.get('erate') is not None:
                srate = request.GET.get('srate')
                erate = request.GET.get('erate')
                if erate == 0:
                    products = Product.objects.filter(selling_price__gt=srate)
                else:
                    products = Product.objects.filter(selling_price__gt=srate, selling_price__lt=erate)
                    
                print(products.query)
            context['product_list'] = products
            cate = products.values_list("category",flat=True).distinct()
            
            
        
            
        context['category_list'] = category_list
        context['brand_list'] = brand_list
        context['color_list'] = color_list
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
        if request.user.is_authenticated and not request.user.is_staff:
            customer =  Customer.objects.get(user_id = request.user) 
            cart_list = Cart.objects.get(customer=customer)
            return render(request,self.template_name,{'allcartprod':cart_list})
        else:
            return redirect("login")
    
class CheckoutView(View):
    template_name = "checkout.html"
    def get(self,request,*args,**kwagrs):
        # return render(request, self.template_name)
        return redirect("cart")
    
    

