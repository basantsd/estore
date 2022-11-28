from django.shortcuts import render
from django.views import View
from site_settings.models import HomeBanner
from .models import Category

class HomeView(View):
    template_name = 'home/index.html'
    def get(self,request,*args,**kwargs):
        homebanner = HomeBanner.objects.filter(is_active=True)
        allcategory = Category.objects.filter(is_active=True)
        context = { 'homebanner':homebanner, 'allcategory': allcategory}
        return render(request,self.template_name,context)
    
class AboutView(View):
    template_name = 'home/about.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)