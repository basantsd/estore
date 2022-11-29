from django.shortcuts import render, redirect
from django.views import View
from site_settings.models import HomeBanner
from .models import Category
from .forms import ContactForm

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
    
class ContactView(View):
    template_name = 'home/contact.html'
    def get(self,request,*args,**kwargs):
        cnform = ContactForm()
        return render(request,self.template_name,{'form':cnform})
    
    def post(self,request,*args,**kwargs):
        cnform = ContactForm(request.POST)
        if cnform.is_valid():
            cnform.save()
            return redirect("contact")
        return render(request,self.template_name,{'form':cnform})