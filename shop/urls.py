from django.urls import path
from shop.views import HomeView,AboutView,ContactView,AjaxView,AjaxUrls,EmptyCart

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('about/',AboutView.as_view(),name="about"),
    path('contact/',ContactView.as_view(),name="contact"),
    path("ajax/",AjaxView.as_view(),name="ajax"),
    path("ajaxcart/",AjaxUrls,name="cartajax"),
    path("emptycart/",EmptyCart,name="emptyCart"),
]


