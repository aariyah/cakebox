from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class User(AbstractUser):

    phone=models.CharField(max_length=100,unique=True)
    address=models.CharField(max_length=200)



class Category(models.Model):

    name=models.CharField(max_length=200,unique=True)
    is_active=models.BooleanField(default=True)

    def _str_(self):
        return self.name
    
    
class Cakes(models.Model):
    name=models.CharField(max_length=200)
    
    options=(
        ("cream cake","cream cake"),
        ("milk cake","milk cake"),
        ("cheese cake","cheese cake"),
        ("cup cake","cup cake"),
        ("plum cake","plum cake"),
        )
    category=models.CharField(max_length=200,choices=options,default="choclate cake")
    image=models.ImageField(upload_to="images")
    options=(("choclate","choclate"),
             ("vanilla","vanilla"),
             ("mango","mango"),
             ("blueberry","blueberry"),
             ("pineapple","pineapple"),
             ("hazelnut","hazelnut"),
             ("almond","almond"),
             ("strawberry","strawberry")
             
             )
    flavours=models.CharField(max_length=200,choices=options,default="choclate")
    
    

    def _str_(self):
        return self.name
    



class CakeVarients(models.Model):
    price=models.PositiveIntegerField()
    color=models.CharField(max_length=100)
    options=(
        ("half kg","half kg"),
        ("1 kg","5 kg"),
        ("3 kg","3 kg"),
        ("4 kg","4 kg"),
        ("5 kg","5 kg"),
        
    )

    size=models.CharField(max_length=200,choices=options,default="1kg")
    options=(
        ("round","round"),
        ("square","square"),
        ("heartshape","heartshape")
    )
    shape=models.CharField(max_length=200,choices=options,default="round")
    cake=models.ForeignKey(Cakes,on_delete=models.CASCADE)



class Offers(models.Model):
     cakevarient=models.ForeignKey(CakeVarients,on_delete=models.CASCADE)
     price=models.PositiveIntegerField()
     start_date=models.DateTimeField()
     due_date=models.DateTimeField()


class Carts(models.Model):
    cakevarient=models.ForeignKey(CakeVarients,on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-place"),
        ("cancelled","cancelled")
    )

    status=models.CharField(max_length=200,choices=options,default="in-cart")
    date=models.DateTimeField(auto_now=True)


class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cakevarient=models.ForeignKey(CakeVarients,on_delete=models.CASCADE)
    options=(
        ("order-placed","order-placed"),
        ("dispatched","dispached"),
        ("cancelled","cancelled"),
        ("in-transit","in-transit"),
        ("delivered","delivered")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    orderd_date=models.DateTimeField(auto_now_add=True)
    expected_date=models.DateField(null=True)
    address=models.CharField(max_length=200)



class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cakevarient=models.ForeignKey(CakeVarients,on_delete=models.CASCADE)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=300)




# purchase
# orderline








