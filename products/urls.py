from django.urls import path, re_path
from products.views import *

urlpatterns = [
    path("shop/",ShopView.as_view(),name="shop"),
    path("shop-details/<slug:pd>/",ShopDetailView.as_view(),name="shop_details"),
    path("cart/",CartView.as_view(),name="cart"),
    path("checkout/",CheckoutView.as_view(),name="checkout"),
]
