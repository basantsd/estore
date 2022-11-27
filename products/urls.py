from django.urls import path
from products.views import *

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('about/',AboutView.as_view(),name="about"),
    path("shop/",ShopView.as_view(),name="shop"),
    path("cart/",CartView.as_view(),name="cart"),
    path("checkout/",CheckoutView.as_view(),name="checkout"),
    path("ajaxurl/",AjaxView.as_view(),name="ajax"),
    
]
