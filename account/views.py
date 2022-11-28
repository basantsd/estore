from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Customer
from account.form import UserCreateFM
from django.contrib import messages


class LoginView(View):
    template_name = 'authentication/login.html'
    def get(self,request,*args,**kwargs):
        fm = AuthenticationForm()
        return render(request,self.template_name,{'form':fm})
    
    def post(self,request,*args,**kwargs):
        fm = AuthenticationForm(request,data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                if Customer.objects.filter(user_id=user,is_email_verfiled=True).exists():
                    login(request,user)
                    return redirect("home")
                else:
                    messages.add_message(request,messages.ERROR,'Please Verify Your Account !')
        return render(request,self.template_name,{'form':fm})
        

class RegisterView(View):
    template_name = 'authentication/register.html'
    def get(self,request,*args,**kwargs):
        fm = UserCreateFM()
        return render(request,self.template_name,{'form':fm})
    
    def post(self,request,*args,**kwargs):
        fm = UserCreateFM(request.POST)
        if fm.is_valid():
            first_name = fm.cleaned_data['first_name']
            last_name = fm.cleaned_data['last_name']
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password1']
            user = User(first_name=first_name,last_name=last_name,email=username,username=username)
            user.set_password(password)
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Account Created Successfully !')
            messages.add_message(request, messages.INFO, 'Verification Mail Sent On Your Email Address !')
            return redirect("login")
        return render(request,self.template_name,{'form':fm})
    
    
class AccountAcivateView(View):
    def get(self,request,*args,**kwargs):
        token = kwargs['token']
        customer = Customer.objects.filter(token=token)
        if customer.exists():
            customer = Customer.objects.get(token=token)
            customer.is_email_verfiled = True
            customer.token = ''
            customer.save()
            messages.add_message(request, messages.SUCCESS, 'Account Verified Successfully !')
        else:
            messages.add_message(request, messages.ERROR, 'Invaild Token !')
        return redirect("login")

    
class ProfileView(View):
    template_name = "home/profile.html"
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    

class LogoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")