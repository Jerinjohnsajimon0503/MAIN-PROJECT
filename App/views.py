from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.models import User

from .models import userProfile,Product,Status,cart,Order,Notification,Category,SubCategory,Payment,ShopKeeper,Rating
# Create your views here.

def homepage(request):
    
    if request.user.is_authenticated:
        profile = userProfile.objects.filter(user = request.user).first()
        products_shop = Product.objects.filter(Q(user = request.user) & Q(approved = True) & Q(sell = False))
       
    else:
        profile = ''
        products_shop = []
        

    
    products = Product.objects.filter(Q(approved = True) & Q(sell = False))

    products_list = []
    try:

        for product in products:
            print(product.name,product.offer)
            car = cart.objects.filter(Q(product = product) & Q(user = request.user)).first()
            print(product)
            if car:
                products_list.append({"name":product.name,"price":product.price,"pk":product.pk,"image":product.image,"cart":True,"user":product.user,"category":product.subcategory,"offer":product.offer,"realPrice":product.realPrice})
            else:
                products_list.append({"name":product.name,"price":product.price,"pk":product.pk,"image":product.image,"cart":False,"user":product.user,"category":product.subcategory,"offer":product.offer,"realPrice":product.realPrice})
    except:
        for product in products:
            
            products_list.append({"name":product.name,"price":product.price,"pk":product.pk,"image":product.image,"cart":False,"user":product.user,"category":product.subcategory,"offer":product.offer,"realPrice":product.realPrice})
            
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user = request.user) 
    else:
        notifications = []      
    print(notifications)
    categories = Category.objects.all()
    subCategories = SubCategory.objects.all()
    return render(request,'index.html',context = {'profile':profile,"products":products_list,"products_shop":products_shop,"notifications":notifications,"categories":categories,"subs":subCategories})


message = 0
reg_error = 0

def checkSignup(request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    
    u = User.objects.filter(username = username).first()
    
    if u == None:
        message = 0
    else:
        message = 1
    
    return JsonResponse({"message":message})

from django.core.files.storage import FileSystemStorage

def register(request):
    file = request.FILES.get('image')
    fss = FileSystemStorage()
    filename = fss.save(file.name,file)
    url = fss.url(filename)

    if request.method == 'POST':
        try:
            user = User.objects.create(username = request.POST.get('username'),email=request.POST.get('email'))
            user.set_password(request.POST.get('password'))
            user.save()

        except:
            pass

        user = User.objects.filter(username=request.POST.get('username')).first()
        
        profile = userProfile.objects.create(user=user)
        profile.phone = request.POST.get('phone')
        profile.image = file
        profile.address = request.POST.get('house') + "," + request.POST.get('location') + "," + request.POST.get('street') + "," +request.POST.get('city') +"," + request.POST.get('pin')
        

        profile.save()
        
            

    return HttpResponseRedirect(reverse('homepage'))

def update(request):
    
        
    profile = userProfile.objects.filter(user=request.user).first()
    profile.phone = request.POST.get('phone')

    profile.address = request.POST.get('address')
   

    profile.save()
        
            

    return HttpResponseRedirect(reverse('homepage'))

def registerShop(request):
    
    file = request.FILES.get('image')
    fss = FileSystemStorage()
    filename = fss.save(file.name,file)
    url = fss.url(filename)
    if request.method == 'POST':
        try:
            user = User.objects.create(username = request.POST.get('username'),email=request.POST.get('email'))
            user.set_password(request.POST.get('password'))
            user.save()
        except:
            pass

        user = User.objects.filter(username=request.POST.get('username')).first()
        
        profile = userProfile.objects.create(user=user)
        profile.shopkeeperPhone = request.POST.get('phone')
        print(request.POST.get('location'))
        profile.shopkeeperAddress = request.POST.get('username') + "," + request.POST.get('city') + "," + request.POST.get('location') + "," + request.POST.get('pin')
        profile.shopkeeperName = request.POST.get('username')
        profile.shopType = request.POST.get('type')
        profile.shopkeeperLocation = request.POST.get('city')
        profile.image = file
        profile.save()
        
        ShopKeeper.objects.create(shopkeeperName = request.POST.get('username'),shopkeeperPhone = request.POST.get('phone'),email =request.POST.get('email'),shopType = request.POST.get('type'),user = user,location = request.POST.get('location'),pin = request.POST.get('pin'),district = request.POST.get('city'),shopkeeperAddress = request.POST.get('username') + "," + request.POST.get('city') + "," + request.POST.get('location') + "," + request.POST.get('pin'))

    return HttpResponseRedirect(reverse('homepage'))

def checkLogin(request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username = username,password = password)
    if user:
        print(username)
        return JsonResponse({"message":0})
            
    else:
        print("No user found")
        return JsonResponse({"message":1})
        

def user_login(request):
   
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username = username,password = password)
        if user:

            if user.is_active:
                login(request, user)
                print("login success!!!")
                return HttpResponseRedirect(reverse('homepage'))
        else:
            
            print("No such user")


    return HttpResponseRedirect(reverse('homepage'))
    
@login_required
def user_logout(request):

    logout(request)


    return HttpResponseRedirect(reverse('homepage'))

def show_login(request):
    return render(request,'login.html')

def show_register(request):
    return render(request,'register.html')


def addProduct(request):

    profile = userProfile.objects.filter(user = request.user).first()

    product = Product.objects.create(user = request.user,
                                     image = request.FILES['image'],
                                     userImage = profile.image.url,
                                     name =  request.POST.get('name'),
                                     stock = request.POST.get('stock'),
                                     price = request.POST.get('price'),
                                     route = request.POST.get('type'),
                                    activeIngredient = request.POST.get('origin'),
                                    manufacturerName  = profile.user.username,
                                    manufacturerAddress = profile.shopkeeperAddress,
                                    manufacturerCountry = profile.shopkeeperLocation,
                                    manufacturerContactNumber = profile.shopkeeperPhone,
                                    description = request.POST.get('description'),
                                    category = request.POST.get('name'),
                                    subcategory = request.POST.get('sub'),
                                    
                                     )

    categories = Category.objects.all()
    found = 0
    for category in categories:
        if request.POST.get('name') == category.name:
            found = 1
            break
    
    if found == 0:
        cate = Category.objects.create(name = request.POST.get('name'))
    else:
        cate = Category.objects.filter(name = request.POST.get('name')).first()
    subcategories = SubCategory.objects.all()
    found = 0

    for sub in subcategories:
        if request.POST.get('name') == sub.name:
            found = 1
            break
    
    if found == 0:
        SubCategory.objects.create(name = request.POST.get('sub'),category = cate)
    

    return HttpResponseRedirect(reverse('homepage'))

