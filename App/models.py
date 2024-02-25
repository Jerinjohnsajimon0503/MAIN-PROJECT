from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class userProfile(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    image = models.ImageField(upload_to='profile_pic',default='sherlock.jpg')
    phone = models.CharField(max_length=500,blank=True)
    address = models.CharField(max_length=5000,blank=True)
    balance = models.IntegerField(default=30000)
    shopkeeperName = models.CharField(max_length=500,blank=True)
    shopkeeperAddress = models.CharField(max_length=500,blank=True)
    shopkeeperPhone = models.IntegerField(default=0)
    shopkeeperLocation = models.CharField(max_length=500,blank=True)
    shopType = models.CharField(max_length=500,blank=True)

    APPROVE = True
    REJECT = False
    CHOICES = (
        (APPROVE, 'Approve'),
        (REJECT, 'Reject')
    )
    
    is_shopkeeper = models.BooleanField(choices=CHOICES, default=REJECT)
    # is_delivery_man = models.BooleanField(default=False)
    rating = models.DecimalField(default=0.0,max_digits=2,decimal_places=1)
    count = models.IntegerField(default=1)
    def __str__(self):
        return self.user.username + " profile"


class Product(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    added_by = models.CharField(max_length=5000,blank=True)
    image = models.ImageField(upload_to='product',default='sherlock.jpg',blank=True)
    userImage = models.CharField(max_length=5000,blank=True)
    
    name = models.CharField(max_length=5000,blank=True)
    dosage = models.CharField(max_length=5000,blank=True)
    price = models.IntegerField(default=0)
    activeIngredient = models.CharField(max_length=5000,blank=True)
    productType = models.CharField(max_length=5000,blank=True)
    description = models.CharField(max_length=50000,blank=True,default = "")
    route = models.CharField(max_length=5000,blank=True)
    manufacturerName = models.CharField(max_length=5000,blank=True)
    manufacturerAddress = models.CharField(max_length=5000,blank=True)
    manufacturerCountry = models.CharField(max_length=5000,blank=True)
    manufacturerContactNumber = models.CharField(max_length=5000,blank=True)
    category = models.CharField(max_length=5000,blank=True)
    subcategory = models.CharField(max_length=5000,blank=True)
    stock = models.DecimalField(default=0.00,max_digits=5,decimal_places=2)
    banned = models.BooleanField(default=False)
    sell = models.BooleanField(default=False)
    approved = models.BooleanField(default=True)
    full_name = models.CharField(max_length = 1000,default = "")
    realPrice = models.IntegerField(default=0)
    offer = models.BooleanField(default=False)
    sellname = models.CharField(max_length = 1000,default = "")
    selladdress = models.CharField(max_length = 1000,default = "")
    sellphone = models.CharField(max_length = 1000,default = "")
    count = models.IntegerField(default=1)
    def __str__(self):
        return self.user.username + "'s product"
    

class Status(models.Model):
    username = models.CharField(max_length=500)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    transaction_address = models.CharField(max_length=5000,blank=True)
    
    def __str__(self):
        return "product status"
    
class Category(models.Model):
    name = models.CharField(max_length=5000)

    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    name = models.CharField(max_length=5000)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.category.name + "'s category : " + self.name
    
class cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.DecimalField(default=0.00,max_digits=5,decimal_places=2)
    price = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username + "'s cart"
    

class Order(models.Model):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    address = models.CharField(max_length=50000,default="")
    date = models.DateTimeField(default=timezone.now)
    to = models.CharField(max_length=50000,default="",blank=True)
    quantity = models.DecimalField(default=0.00,max_digits=5,decimal_places=2)
    price = models.IntegerField(default=0)
    status = models.CharField(max_length=1200,default="Pending")

    def __str__(self):
        return self.user.username +  "'s order"



class Payment(models.Model):
    from_user = models.CharField(max_length=50000, default="")
    to_user = models.CharField(max_length=50000, default="")
    amount = models.CharField(max_length=50000, default="")
    product = models.CharField(max_length=50000, default="")
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        formatted_date = self.date.strftime('%Y-%m-%d %H:%M:%S')  # Format the date as 'YYYY-MM-DD HH:MM:SS'
        return f"{self.from_user} paid Rs {self.amount} to {self.to_user} for the product {self.product} on {formatted_date}"



class Notification(models.Model):
    
    product_pk = models.IntegerField(default = 0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.CharField(max_length=5000,blank=True,default ="")
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username + ' notification'
    

class ShopKeeper(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    shopkeeperName = models.CharField(max_length=255)
    shopkeeperPhone = models.CharField(max_length=20)
    shopkeeperAddress = models.CharField(max_length=255)
    shopType = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    # street = models.CharField(max_length=1000)
    location = models.CharField(max_length=1000)
    district = models.CharField(max_length=1000)
    email = models.EmailField()
   
    is_shopkeeper = models.BooleanField(default=False)

    def __str__(self):
        return self.shopkeeperName

class Customer(models.Model):

    username = models.CharField(max_length=500,blank=True)
    email = models.CharField(max_length=500,blank=True)
    phone = models.CharField(max_length=500,blank=True)
    address = models.CharField(max_length=5000,blank=True)
    balance = models.IntegerField(default=30000)
    
    
    def __str__(self):
        return self.user.username + " profile"
    
@receiver(post_save, sender=ShopKeeper)
def update_user_profile(sender, instance, **kwargs):
    user_profile = userProfile.objects.get(user=instance.user)
    user_profile.is_shopkeeper = instance.is_shopkeeper
    user_profile.save()

class Rating(models.Model):
    
    user = models.CharField(max_length=20)
    product = models.CharField(max_length=20)
    rating = models.IntegerField(default=0)
    def __str__(self):
        return self.user