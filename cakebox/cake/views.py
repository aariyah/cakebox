from django.shortcuts import render,redirect

from django.views.generic import CreateView,FormView
from cake.forms import RegistrationForm,LoginForm
from cake.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


class SignUpView(CreateView):


    template_name="cake/register.html"
    form_class=RegistrationForm
    model=User
    success_url=reverse_lazy("signin")


    def form_valid(self,form):
        messages.success(self.request,"account created")
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.error(self.request,"failed to create account")
        return super().form_invalid(form)

class SignInView(FormView):
    template_name="cake/login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=logout(request.POST)

        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)   
            if usr:
                login(request,usr)
                messages.success(request,"login success")
                return redirect("signin")
            else:
                 messages.error(request,"invalid credentials!!!")
                 return render(request,self.template_name,{"form":form})

        
