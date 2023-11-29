from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,ListView,DetailView,UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


from cake.forms import RegistrationForm,LoginForm,CategoryCreateForm,CakeAddForm,CakeVarientForm,OfferForm
from cake.models import User,Category,Cakes,CakeVarients,Offers


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
        form=LoginForm(request.POST)

        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)   
            if usr:
                login(request,usr)
                messages.success(request,"login successfully")
                return redirect("signin")
            else:
                 messages.error(request,"invalid credentials!!!")
                 return render(request,self.template_name,{"form":form})

        
class CategoryCreateView(CreateView,ListView,DetailView):
    
    template_name="cake/category_add.html"
    form_class=CategoryCreateForm
    model=Category
    context_object_name="categories"
    success_url=reverse_lazy("category-add")

    def form_valid(self, form):
        messages.success(self.request,"category created successfully")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,"category adding failed")
        return super().form_invalid(form)
    
    def get_queryset(self):
        return Category.objects.filter(is_active=True)
    

def remove_category(request,*args,**kwargs):
    id=kwargs.get("pk")
    Category.objects.filter(id=id).update(is_active=False)
    messages.success(request,"remove-category")
    return redirect("category-add")
    

class CakeCreateView(CreateView):

    template_name="cake/cake_add.html"
    model=Cakes
    form_class=CakeAddForm
    success_url=reverse_lazy("cake-add")

    def form_valid(self,form):
        messages.success(self.request,"cake has been added")
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,"cake adding failed")
        return super().form_invalid(form)
    

class CakeListView(ListView):
    template_name="cake/cake_list.html"
    model=Cakes
    context_object_name="cakes"



class CakeUpdateView(UpdateView):
    template_name="cake/cake_edit.html"
    model=Cakes
    form_class=CakeAddForm
    success_url=reverse_lazy("cake-list")

    def form_valid(self,form):
        messages.success(self.request,"cakes updated succesfully")
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,"cake updating failed")
        return super().form_invalid(form)
    

def remove_cakeview(request,*args,**kwargs):
    id=kwargs.get("pk")
    Cakes.objects.filter(id=id).delete()
    return redirect("cake-list")


class CakeVarientCreateView(CreateView):
    template_name="cake/cakevarient_add.html"
    form_class=CakeVarientForm
    model=CakeVarients
    success_url=reverse_lazy("cake-list")

    def form_valid(self, form):
        id=self.kwargs.get("pk")
        obj=Cakes.objects.get(id=id)
        form.instance.cake=obj
        messages.success(self.request,"varient has been added")
    
        return super().form_valid(form)


class CakeDetailView(DetailView):
    template_name="cake/cake_detail.html"
    model=Cakes
    context_object_name="cake"



class CakeVarientUpdateView(UpdateView):
    template_name="cake/cakevarient_edit.html"
    form_class=CakeVarientForm
    model=CakeVarients
    success_url=reverse_lazy("cake-list")
    def form_valid(self,form):
        messages.success(self.request,"cakevarient updated succesfully")
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,"cakevarient updating failed")
        return super().form_invalid(form)
    



def remove_varient(request,*args,**kwargs):
    id=kwargs.get("pk")
    CakeVarients.objects.filter(id=id).delete()
    return redirect("cake-list")




class OfferCreateView(CreateView):
    template_name="cake/offer_add.html"
    form_class=OfferForm
    model=Offers
    success_url=reverse_lazy("cake-list")
    def form_valid(self,form):
        id=self.kwargs.get("pk")
        obj=CakeVarients.objects.get(id=id)
        form.instance.clothvarient=obj

        messages.success(self.request,"offer has been added")
        return super().form_valid(form)

    def form_invalid(self,form):
        messages.error(self.request,"offer adding failed")
        return super().form_invalid(form)