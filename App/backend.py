from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.models import User

from .models import *
# Create your views here.

def homepage(request):
    
    if request.user.is_authenticated:
        profile = userProfile.objects.filter(user = request.user).first()
        products_shop = Product.objects.filter(Q(user = request.user) & Q(approved = True) & Q(sell = False))
        all_chats_to = []
        chats = Chat.objects.filter(to_user = request.user)
        
        for chat in chats:
            pro = userProfile.objects.filter(user = User.objects.filter(username = chat.from_user).first()).first()
            all_chats_to.append({"username":chat.from_user,"image":pro.image.url,"message":"mesg.message"})
        
        chats2 = Chat.objects.filter(from_user = request.user)
        for chat in chats2:
            pro = userProfile.objects.filter(user = User.objects.filter(username = chat.to_user).first()).first()

            all_chats_to.append({"username":chat.to_user,"image":pro.image.url,"message":"mesg.message"})
    else:
        profile = ''
        products_shop = []
        all_chats_to = []

    comments = Comment.objects.all()
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
    return render(request,'index.html',context = {'profile':profile,"products":products_list,"products_shop":products_shop,'chats':all_chats_to,"comments":comments,"notifications":notifications,"categories":categories,"subs":subCategories})


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
        Chat.objects.create(from_user = request.POST.get('username'),to_user = "Herbalist")

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
                                     stock = request.POST.get('dosage'),
                                     price = request.POST.get('price'),
                                     route = request.POST.get('route'),
                                    activeIngredient = request.POST.get('activeIngredient'),
                                    manufacturerName  = profile.user.username,
                                    manufacturerAddress = profile.shopkeeperAddress,
                                    manufacturerCountry = profile.shopkeeperLocation,
                                    manufacturerContactNumber = profile.shopkeeperPhone,
                                    description = request.POST.get('description'),
                                    category = request.POST.get('name'),
                                    subcategory = request.POST.get('sub'),
                                    # stock = request.POST.get('')
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

def productView(request,pk):
    
    profile = userProfile.objects.filter(user = request.user).first()
    product = Product.objects.filter(pk = pk).first()
    ct = cart.objects.filter(user = request.user,product = product).first()
    
    products = Product.objects.filter(Q(user = product.user) & Q(approved = True))
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user = request.user) 
    else:
        notifications = []
    categories = Category.objects.all()
    subCategories = SubCategory.objects.all()
    #----------------------------------------------------------------
    cms = commentUser.objects.filter(product = product)
    # print(cms.first().text)
    return render(request,'productView.html',{"product":product,"profile":profile,"cart":ct,"products":products,"name":product.name,"notifications":notifications,"categories":categories,"subs":subCategories,"commentsall":cms})



def status(request,pk):
    


    return HttpResponseRedirect(reverse('homepage'))


def addToCart(request):
    product = Product.objects.filter(pk = request.POST.get('pk')).first()
    price = product.price
    total = 0
    
    if product.stock >= float(request.POST.get('quantity')):
        out = 0
    else:
        out = 1
    if out == 0:
        try:
            for i in range(0,int(request.POST.get('quantity'))):
                total = total + price
            print("heyyy")
            ct = cart.objects.create(user = request.user,product = product,quantity = request.POST.get('quantity'),price = total)
        except:
            total = price / 2
            ct = cart.objects.create(user = request.user,product = product,quantity = request.POST.get('quantity'),price = total)
 
    return JsonResponse({"success":1,"out":out})


def carts(request):
    profile = userProfile.objects.filter(user = request.user).first()
    ct = cart.objects.filter(user = request.user)
    products = []
    
    for c in ct:

        products.append(c.product)
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user = request.user) 
    else:
        notifications = []
    return render(request,'cart.html',{"cart":products,"profile":profile,"carts":ct,"notifications":notifications})



def shop(request):
    
    if request.user.is_authenticated:
        profile = userProfile.objects.filter(user = request.user).first()
        products_shop = Product.objects.filter(Q(user = request.user) & Q(approved = True) & Q(sell = False))
    else:
        profile = ''
        products_shop = Product.objects.all()

    products_herb = userProfile.objects.filter(shopType = "Herb")
    products_veg = userProfile.objects.filter(shopType = "Vegetable")
    products_fruit = userProfile.objects.filter(shopType = "Fruits")
    herbs = []
    vegs = []
    fruits = []
    #print(products_herb[0].shopkeeperPhone)
    products_list = []
    products_list_veg = []
    products_list_fruit = []

    for doc in products_herb:
        
        # app = Appointment.objects.filter(Q(username = request.user.username) & Q(doctor = doc.user.username) & Q(done = False)).first()
        rating = Rating.objects.filter(Q(user = request.user.username) & Q(doctor = doc.user.username)).first()
        herbs.append({"user":doc.user,"image":doc.image,"first_name":doc.user.first_name,"last_name":doc.user.last_name,"shopkeeperAddress":doc.shopkeeperAddress,"shopkeeperPhone":doc.shopkeeperPhone,"rating":doc.rating,"rated":True if rating else False})
    
    for doc in products_veg:
        
        # app = Appointment.objects.filter(Q(username = request.user.username) & Q(doctor = doc.user.username) & Q(done = False)).first()
        rating = Rating.objects.filter(Q(user = request.user.username) & Q(doctor = doc.user.username)).first()
        vegs.append({"user":doc.user,"image":doc.image,"first_name":doc.user.first_name,"last_name":doc.user.last_name,"shopkeeperAddress":doc.shopkeeperAddress,"shopkeeperPhone":doc.shopkeeperPhone,"rating":doc.rating,"rated":True if rating else False})
    
    for doc in products_fruit:
        
        # app = Appointment.objects.filter(Q(username = request.user.username) & Q(doctor = doc.user.username) & Q(done = False)).first()
        rating = Rating.objects.filter(Q(user = request.user.username) & Q(doctor = doc.user.username)).first()
        fruits.append({"user":doc.user,"image":doc.image,"first_name":doc.user.first_name,"last_name":doc.user.last_name,"shopkeeperAddress":doc.shopkeeperAddress,"shopkeeperPhone":doc.shopkeeperPhone,"rating":doc.rating,"rated":True if rating else False})
    
    # for product in products_herb:
    #     car = cart.objects.filter(Q(product = product) & Q(user = request.user)).first()
    #     if car:
    #         products_list.append({"name":product.name,"price":product.price,"pk":product.pk,"image":product.image,"cart":True,"user":product.user})
    #     else:
    #         products_list.append({"name":product.name,"price":product.price,"pk":product.pk,"image":product.image,"cart":False,"user":product.user})
   
    # for product in products_veg:
    #     car = cart.objects.filter(Q(product = product) & Q(user = request.user)).first()
    #     if car:
    #         products_list_veg.append({"name":product.name,"price":product.price,"pk":product.pk,"image":product.image,"cart":True,"user":product.user})
    #     else:
    #         products_list_veg.append({"name":product.name,"price":product.price,"pk":product.pk,"image":product.image,"cart":False,"user":product.user})

    # for product in products_fruit:
    #     car = cart.objects.filter(Q(product = product) & Q(user = request.user)).first()
    #     if car:
    #         products_list_fruit.append({"name":product.name,"price":product.price,"pk":product.pk,"image":product.image,"cart":True,"user":product.user})
    #     else:
    #         products_list_fruit.append({"name":product.name,"price":product.price,"pk":product.pk,"image":product.image,"cart":False,"user":product.user})
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user = request.user) 
    else:
        notifications = []
    categories = Category.objects.all()
    subCategories = SubCategory.objects.all()
    return render(request,'shop.html',context = {'profile':profile,"products":herbs,"products_shop":products_shop,"fruits":fruits,"veg":vegs,"notifications":notifications,"categories":categories,"subs":subCategories})



import decimal
def buy(request):
    from_user = userProfile.objects.filter(user = request.user).first()
    product = Product.objects.filter(pk = request.POST.get('pk')).first()
    # print("Quantity",request.POST.get('quantity'))
    if from_user.balance - int(request.POST.get('price')) > 0 and product.stock >= float(request.POST.get('quantity')):
        success = 1
    else:
        success = 0
    print(success)
    if product.stock >= float(request.POST.get('quantity')):
        print("----------------------+++")
        if from_user.balance - int(request.POST.get('price')) > 0:
            to = userProfile.objects.filter(user = product.user).first()
            to.balance = to.balance + int(request.POST.get('price'))
            from_user.balance = from_user.balance - (int(request.POST.get('price')) + 15)
            to.save()
            from_user.save()
            success = 1
            quantity_str = request.POST.get('quantity')
            quantity = decimal.Decimal(quantity_str)  # Convert the string to a decimal number

            product.stock = decimal.Decimal(product.stock) - quantity
            print("--------------------++++++++++++++++")
            product.save()
            admin = userProfile.objects.filter(user = User.objects.filter(username = "admin").first()).first()
            admin.balance = admin.balance + 15
            admin.save()
            Payment.objects.create(from_user = request.user.username,to_user = product.user.username ,amount = int(request.POST.get('price')) + 15,product = product.name)
            Notification.objects.create(user = request.user,message = "Your order of " + product.name + " has been placed and will be delivered to you soon.",product_pk = product.pk)
        else:
            success = 0
        out = 0

        
    else:
        out = 1
        

    order = Order.objects.create(user = request.user,product = product,address = from_user.address,quantity = request.POST.get('quantity'),price = int(request.POST.get('price')) + 15,to = product.user.username)

    return JsonResponse({"success":success,"out":out})


def check(request):
    from_user = userProfile.objects.filter(user = request.user).first()
    product = Product.objects.filter(pk = request.POST.get('pk')).first()
    # print("Quantity",request.POST.get('quantity'))
    if from_user.balance - int(request.POST.get('price')) > 0 and product.stock >= float(request.POST.get('quantity')):
        success = 1
    else:
        success = 0
    print(success)
    if product.stock >= float(request.POST.get('quantity')):
        if from_user.balance - float(request.POST.get('price')) > 0:
            
            success = 1
            
        else:
            success = 0
        out = 0
        
    else:
        out = 1
        

    # order = Order.objects.create(user = request.user,product = product,address = from_user.address,quantity = request.POST.get('quantity'),price = request.POST.get('price'),to = product.user.username)

    return JsonResponse({"success":success,"out":out})


def buyAdd(request):
    from_user = userProfile.objects.filter(user = request.user).first()
    product = Product.objects.filter(pk = request.POST.get('pk')).first()
    # print("Quantity",request.POST.get('quantity'))
    
    if product.stock >= int(request.POST.get('quantity')):
        out = 0
        order = Order.objects.create(user = request.user,product = product,address = from_user.address,quantity = request.POST.get('quantity'),price = request.POST.get('price'),to = product.user.username)
        product.stock = product.stock - int(request.POST.get('quantity'))
        product.save()
        
    else:
        out = 1
        
    print("Successfully placed order",from_user.address)
    return JsonResponse({"success":1,"out":out})



def buy2(request):
    from_user = userProfile.objects.filter(user = request.user).first()
    product = Product.objects.filter(pk = request.POST.get('pk')).first()
    if from_user.balance - int(request.POST.get('price')) > 0:
        to = userProfile.objects.filter(user = product.user).first()
        to.balance = to.balance + int(request.POST.get('price'))
        from_user.balance = from_user.balance - int(request.POST.get('price'))
        to.save()
        from_user.save()
        success = 1
    else:
        success = 0

    try:
        ct = cart.objects.filter(user = request.user,product = product)
        ct.delete()
    except:
        pass

    order = Order.objects.create(user = request.user,product = product,address = from_user.address,quantity = request.POST.get('quantity'),price = request.POST.get('price'),to = product.user.username)

    return JsonResponse({"success":success})


def orders(request):
    
    
    profile = userProfile.objects.filter(user = request.user).first()

    

    print(profile.is_shopkeeper)
    if not profile.is_shopkeeper:
        orders_all = Order.objects.filter(user = request.user).order_by('-date')

    else:
        orders_all = Order.objects.filter(to = request.user.username).order_by('-date')
    print(orders_all)
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user = request.user) 
    else:
        notifications = []
    categories = Category.objects.all()
    subCategories = SubCategory.objects.all()
    return render(request,'orders.html',context = {'profile':profile,"orders":orders_all,"notifications":notifications,"categories":categories,"subs":subCategories})

def search(request):
    
    if request.user.is_authenticated:
        profile = userProfile.objects.filter(user = request.user).first()

    else:
        profile = ''
    
    orders_all = Product.objects.filter(Q(full_name__icontains = request.POST.get('query')) | Q(category = request.POST.get('query')))
    products_list = []
    try:

        for product in orders_all:
            if product.price <= int(request.POST.get('price')):
                car = cart.objects.filter(Q(product = product) & Q(user = request.user)).first()
                if car:
                    products_list.append({"name":product.name,"price":product.price,"pk":product.pk,"image":product.image,"cart":True,"user":product.user})
                else:
                    products_list.append({"name":product.name,"price":product.price,"pk":product.pk,"image":product.image,"cart":False,"user":product.user})
            else:
                pass
    except:
        products_list = orders_all 

    print(orders_all)
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user = request.user) 
    else:
        notifications = []
    categories = Category.objects.all()
    subCategories = SubCategory.objects.all()
    return render(request,'search.html',context = {'profile':profile,"products":products_list,"categories":categories,"subs":subCategories})

def delete(request,pk):
    
    product = Product.objects.filter(pk = pk).first()
    product.delete()
    return HttpResponseRedirect(reverse('homepage'))



def sendMsg(request):

    chat = Chat.objects.filter(Q(from_user = request.POST.get('from_user')) & Q(to_user = request.POST.get('to_user'))).first()
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="You: "+request.POST.get("message"),
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"]
        )
    if chat:
        # chatObj = Chat.objects.create(from_user = request.POST.get('from_user') ,to_user = request.POST.get('to_user'))
        message = Message.objects.create(chat = chat,message = request.POST.get("message"),from_user = request.POST.get('from_user') ,to_user = request.POST.get('to_user'))
        message = Message.objects.create(chat = chat,message = str(response["choices"][0]["text"]).replace("\n\n","").replace("Bot:",""),from_user = "Herbalist" ,to_user = request.POST.get('from_user'))

    else:
        chat = Chat.objects.filter(Q(from_user = request.POST.get('to_user')) & Q(to_user = request.POST.get('from_user'))).first()
        message = Message.objects.create(chat = chat,message = request.POST.get("message"),from_user = request.POST.get('from_user') ,to_user = request.POST.get('to_user'))

   
    return JsonResponse({"result":str(response["choices"][0]["text"]).replace("\n\n","").replace("Bot:","")})


import os
import openai

# openai.api_key = "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"

def sendMsg1(request):

    chat = Chat.objects.filter(Q(from_user = request.POST.get('from_user')) & Q(to_user = request.POST.get('to_user'))).first()
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="You: "+request.POST.get("message"),
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"]
        )
    if chat:
        # chatObj = Chat.objects.create(from_user = request.POST.get('from_user') ,to_user = request.POST.get('to_user'))
        message = Message.objects.create(chat = chat,message = request.POST.get("message"),from_user = request.POST.get('from_user') ,to_user = request.POST.get('to_user'))
        message = Message.objects.create(chat = chat,message = str(response["choices"][0]["text"]).replace("\n\n","").replace("Bot:",""),from_user = "Herbalist" ,to_user = request.POST.get('from_user'))

    else:
        chat = Chat.objects.filter(Q(from_user = request.POST.get('to_user')) & Q(to_user = request.POST.get('from_user'))).first()
        message = Message.objects.create(chat = chat,message = request.POST.get("message"),from_user = request.POST.get('from_user') ,to_user = request.POST.get('to_user'))

   
    return JsonResponse({"result":str(response["choices"][0]["text"]).replace("\n\n","").replace("Bot:","")})

def showMessages(request):

    
    chat = Chat.objects.filter(Q(from_user = request.POST.get('from_user')) & Q(to_user = request.POST.get("to_user"))).first()
    
    if chat:
        chat = Chat.objects.filter(Q(from_user = request.POST.get('from_user')) & Q(to_user = request.POST.get("to_user"))).first()

    else:
        chat = Chat.objects.filter(Q(from_user = request.POST.get('to_user')) & Q(to_user = request.POST.get("from_user"))).first()

    user = User.objects.filter(username = request.POST.get('to_user')).first()
    profile = userProfile.objects.filter(user = user).first()
    print(profile)
    messages = Message.objects.filter(chat = chat).all()

    msg_list = []
    for message in messages:
        m = {"from_user":message.from_user,"to_user":message.to_user,"message":message.message}

        msg_list.append(m)


    return JsonResponse({"message":msg_list,"image":profile.image.url})

def comment(request):

    Comment.objects.create(user = request.user,image = userProfile.objects.filter(user = request.user).first().image.url,comment = request.POST.get('comment'))

    return HttpResponseRedirect(reverse('homepage'))


def stock(request):
    
    product = Product.objects.filter(pk = request.POST.get('pk')).first()
    # print("Quantity",request.POST.get('quantity'))
    
    product.stock = int(request.POST.get('stock'))
    product.save()
        
    return JsonResponse({"stock":product.stock,"out":1})


def sell(request):
    
    product = Product.objects.filter(pk = request.POST.get('pk')).first()
    profile = userProfile.objects.filter(user = product.user).first()
    userProf = userProfile.objects.filter(user = request.user).first()
    print(profile.shopkeeperAddress)
    sell = Product.objects.create(user = product.user,
                                     image = request.FILES['image'],
                                     userImage = profile.image.url,
                                     name =  request.POST.get('name'),
                                    
                                        stock = request.POST.get('stock'),
                                        manufacturerName  = profile.user.username,
                                        manufacturerAddress = profile.shopkeeperAddress,
                                        productType = profile.shopType,
                                        sell = True,
                                        approved = False ,
                                        manufacturerContactNumber = profile.shopkeeperPhone,
                                        manufacturerCountry = "Kerala",
                                        added_by = request.user.username,
                                        subcategory = request.POST.get('sub'),
                                        activeIngredient = request.POST.get('origin'),
                                        sellname = userProf.user.username,
                                        selladdress = userProf.address,
                                        sellphone = userProf.phone,
                                     )
        
    return productView(request,request.POST.get('pk'))


def notifications(request):
    
    
    profile = userProfile.objects.filter(user = request.user).first()
    products_list = Product.objects.filter(Q(user = request.user) & Q(sell = True) & Q(approved = False) & Q(banned = False))
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user = request.user) 
    else:
        notifications = []

    return render(request,'notifications.html',context = {'profile':profile,"products":products_list,"notifications":notifications})


def approve(request):
    
    product = Product.objects.filter(pk = request.POST.get('pk')).first()
    product.price = request.POST.get('price')
    product.sell = False 
    product.approved = True 
    product.save()
    us = User.objects.filter(username = product.added_by).first()
    to = userProfile.objects.filter(user = us).first()
    from_user = userProfile.objects.filter(user = request.user).first()
    to.balance = to.balance + int(request.POST.get('price'))
    from_user.balance = from_user.balance - int(request.POST.get('price'))
    to.save()
    from_user.save()
    print(request.POST.get('price'))
    return HttpResponseRedirect(reverse('notifications'))


def reject(request,pk):
    
    product = Product.objects.filter(pk = pk).first()
    
    product.sell = True 
    product.approved = False 
    product.banned = True
    product.save()

    Notification.objects.create(user = User.objects.filter(username = product.sellname).first(),message = "Your uploaded product " + product.name + " has been rejected by shopkeeper " + request.user.username,product_pk = product.pk)

    
    return HttpResponseRedirect(reverse('notifications'))


def cartView(request,pk):
    
    profile = userProfile.objects.filter(user = request.user).first()
    ct = cart.objects.filter(pk = pk).first()
    product = Product.objects.filter(pk = ct.product.pk).first()
    print(product)
    ct = cart.objects.filter(user = request.user,product = product).first()
    
    products = Product.objects.filter(Q(user = product.user) & Q(approved = True))
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user = request.user) 
    else:
        notifications = []
    #----------------------------------------------------------------
    return render(request,'viewCart.html',{"product":product,"profile":profile,"cart":ct,"products":products,"name":product.name,"notifications":notifications})

def cartDelete(request,pk):
    
    profile = userProfile.objects.filter(user = request.user).first()
    ct = cart.objects.filter(pk = pk).first()
    ct.delete()
    #----------------------------------------------------------------
    return HttpResponseRedirect(reverse('cart'))



def cancelOrder(request,pk):
    
    profile = userProfile.objects.filter(user = request.user).first()
    ct = Order.objects.filter(pk = pk).first()
    prod = Product.objects.filter(pk = ct.product.pk).first()
    print(prod)
    prod.stock = prod.stock + ct.quantity
    prod.save()
    print(profile.balance)
    noti = Notification.objects.filter(Q(user =  request.user) & Q(product_pk = prod.pk)).first()
    noti.delete()
    profile.balance = profile.balance + ct.price
    profile.save()
    profile = userProfile.objects.filter(user = prod.user).first()
    profile.balance = profile.balance - ct.price
    profile.save()
    print(profile.balance)
    ct.status = "Cancelled"
    ct.save()

    return HttpResponseRedirect(reverse('orders'))

def deleteOrder(request,pk):
    
    profile = userProfile.objects.filter(user = request.user).first()
    ct = Order.objects.filter(pk = pk).first()
    
    ct.delete()

    return HttpResponseRedirect(reverse('orders'))

def shopView(request):
    
    if request.user.is_authenticated:
        profile = userProfile.objects.filter(user = request.user).first()
        products_shop = Product.objects.filter(Q(user = request.user) & Q(approved = True) & Q(sell = False))
        all_chats_to = []
        chats = Chat.objects.filter(to_user = request.user)
        
        for chat in chats:
            pro = userProfile.objects.filter(user = User.objects.filter(username = chat.from_user).first()).first()
            all_chats_to.append({"username":chat.from_user,"image":pro.image.url,"message":"mesg.message"})
        
        chats2 = Chat.objects.filter(from_user = request.user)
        for chat in chats2:
            pro = userProfile.objects.filter(user = User.objects.filter(username = chat.to_user).first()).first()

            all_chats_to.append({"username":chat.to_user,"image":pro.image.url,"message":"mesg.message"})
    else:
        profile = ''
        products_shop = []
        all_chats_to = []

    comments = Comment.objects.all()
    use = User.objects.filter(username = request.POST.get('name')).first()
    print(use)
    products = Product.objects.filter(user = use)

    products_list = []
    

    for product in products:
        car = cart.objects.filter(Q(product = product) & Q(user = request.user)).first()
        if car:
            products_list.append({"name":product.name,"price":product.price,"pk":product.pk,"image":product.image,"cart":True,"user":product.user,"category":product.subcategory,"offer":product.offer,"realPrice":product.realPrice})
        else:
            products_list.append({"name":product.name,"price":product.price,"pk":product.pk,"image":product.image,"cart":False,"user":product.user,"category":product.subcategory,"offer":product.offer,"realPrice":product.realPrice})
    

    print(products_list)        
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user = request.user) 
    else:
        notifications = []
    categories = Category.objects.all()
    subCategories = SubCategory.objects.all()
    return render(request,'shopView.html',context = {'profile':profile,"products":products_list,"products_shop":products_shop[:4],'chats':all_chats_to,"comments":comments,"username":request.POST.get('name'),"notifications":notifications,"categories":categories,"subs":subCategories})


def checkCategory(request):
    category = Category.objects.filter(pk = request.POST.get('pk')).first()
    subs = SubCategory.objects.filter(category = category)
    subs_final = []
    for sub in subs:
        subs_final.append(sub.name)

    return JsonResponse({"message":message,"categories":subs_final})


def bill(request):
    profile = userProfile.objects.filter(user = request.user).first()
    ct = cart.objects.filter(user = request.user)
    products = []
    # print("-------------",request.POST.get('pks'))
    pks_all = request.POST.get('pks')
    print(pks_all)
    if not pks_all:  
        pks = []
    elif ',' not in pks_all:  
        pks = [pks_all]
    else:
        pks = pks_all.split(',')
    count = 0
    total = 0
    for c in ct:
        # print(c.quantity)
        for p in pks:
            # print("prod ", c.pk)
            # print("my ", p)
            if int(c.pk) == int(p):
                print("============")
                products.append(c)
                count = count + 1
                total = total + c.price 
                print("----"+str(total))
            else:
                pass
    # total = total + 15
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user = request.user) 
    else:
        notifications = []
    # total = 0
    # for car in ct:
    #     total = total + car.price
    print("--------------------------------------") 
    # print(products[0])
    return render(request,'bill.html',{"cart":products,"profile":profile,"carts":products,"notifications":notifications,"total":total,"count":count,'pks':request.POST.get('pks')})

def buyAll(request):
    products = []
    
    ct = cart.objects.filter(user = request.user)
    for c in ct:
        products.append(c.product)

    from_user = userProfile.objects.filter(user = request.user).first()
    
    total = 0
    for car in ct:
        total = total + car.price
    
    from_user.balance = from_user.balance - (total + 15)
    from_user.save()
    admin = userProfile.objects.filter(user = User.objects.filter(username = "admin").first()).first()
    admin.balance = admin.balance + 15
    admin.save()
    for c in ct:
       c.product.stock = c.product.stock - c.quantity
       c.product.save()
       to_user = userProfile.objects.filter(user = c.product.user).first()
       to_user.balance = to_user.balance + c.price 
       to_user.save()
       Payment.objects.create(from_user = request.user.username,to_user = c.user.username ,amount = int(c.price) + 15,product = c.product.name)

       Order.objects.create(user = request.user,product = c.product,address = from_user.address,quantity = c.quantity,price = c.price,to = c.product.user.username)
       Notification.objects.create(user = request.user,message = "Your order of " + c.product.name + " has been placed and will be delivered to you soon.",product_pk = c.product.pk)
       c.delete()
    return JsonResponse({"success":1})

def buyAllBill(request):
    pks_all = request.POST.get('pks')
    if not pks_all:  
        pks = []
    elif ',' not in pks_all:  
        pks = [pks_all]
    else:
        pks = pks_all.split(',')

    for p in pks:
        c = cart.objects.filter(pk=int(p)).first()

        if c.pk == int(p):
            from_user = userProfile.objects.filter(user=request.user).first()
            from_user.balance = from_user.balance - (c.price + 15)
            from_user.save()

            admin = userProfile.objects.filter(user=User.objects.filter(username="admin").first()).first()
            admin.balance = admin.balance + 15
            admin.save()

            c.product.stock = c.product.stock - c.quantity
            c.product.save()

            to_user = userProfile.objects.filter(user=c.product.user).first()
            to_user.balance = to_user.balance + c.price 
            to_user.save()

            Payment.objects.create(from_user=request.user.username, to_user=c.user.username, amount=int(c.price) + 15, product=c.product.name)

            Order.objects.create(user=request.user, product=c.product, address=from_user.address, quantity=c.quantity, price=c.price, to=c.product.user.username)
            
            Notification.objects.create(user=request.user, message="Your order of " + c.product.name + " has been placed and will be delivered to you soon.", product_pk=c.product.pk)

            c.delete()

    return JsonResponse({"success": 1})


def checkAll(request):
    ct = cart.objects.filter(user = request.user)
    products = []
    
    for c in ct:
        products.append(c.product)

    from_user = userProfile.objects.filter(user = request.user).first()
    
    total = 0
    for car in ct:
        total = total + car.price
    
    if from_user.balance < total:
        success = 0
    else:
        success = 1
    message = ""
    out = 0
    for c in ct:
        if c.product.stock < c.quantity:
            message  = message + c.product.name + ", "
            out = 1
    print(message)
    # order = Order.objects.create(user = request.user,product = product,address = from_user.address,quantity = request.POST.get('quantity'),price = request.POST.get('price'),to = product.user.username)

    return JsonResponse({"success":success,"out":out,"message":message})



def cartDeleteAll(request,pk):
    
    profile = userProfile.objects.filter(user = request.user).first()
    ct = cart.objects.filter(pk = pk).first()
    ct.delete()
    #----------------------------------------------------------------
    return HttpResponseRedirect(reverse('bill'))


def buyAllAdd(request):
    ct = cart.objects.filter(user = request.user)
    products = []
    
    for c in ct:
        products.append(c.product)

    from_user = userProfile.objects.filter(user = request.user).first()
    
    total = 0
    for car in ct:
        total = total + car.price
    
    # from_user.balance = from_user.balance - total 
    # from_user.save()
    for c in ct:
       c.product.stock = c.product.stock - c.quantity
       c.product.save()
       Order.objects.create(user = request.user,product = c.product,address = from_user.address,quantity = c.quantity,price = c.price,to = c.product.user.username)
       Notification.objects.create(user = request.user,message = "Your order of " + c.product.name + " has been placed and will be delivered to you soon.",product_pk = c.product.pk)
       c.delete()
    return JsonResponse({"success":1})


def offers(request):
    
    if request.user.is_authenticated:
        profile = userProfile.objects.filter(user = request.user).first()
        products_shop = Product.objects.filter(Q(user = request.user) & Q(approved = True) & Q(sell = False))
        all_chats_to = []
        chats = Chat.objects.filter(to_user = request.user)
        
        for chat in chats:
            pro = userProfile.objects.filter(user = User.objects.filter(username = chat.from_user).first()).first()
            all_chats_to.append({"username":chat.from_user,"image":pro.image.url,"message":"mesg.message"})
        
        chats2 = Chat.objects.filter(from_user = request.user)
        for chat in chats2:
            pro = userProfile.objects.filter(user = User.objects.filter(username = chat.to_user).first()).first()

            all_chats_to.append({"username":chat.to_user,"image":pro.image.url,"message":"mesg.message"})
    else:
        profile = ''
        products_shop = []
        all_chats_to = []

    comments = Comment.objects.all()
    use = User.objects.filter(username = request.POST.get('name')).first()
    print(use)
    products = Product.objects.filter(offer = True)

    products_list = []
    

    for product in products:
        car = cart.objects.filter(Q(product = product) & Q(user = request.user)).first()
        if car:
            products_list.append({"name":product.name,"price":product.price,"pk":product.pk,"image":product.image,"cart":True,"user":product.user,"category":product.subcategory,"offer":product.offer,"realPrice":product.realPrice})
        else:
            products_list.append({"name":product.name,"price":product.price,"pk":product.pk,"image":product.image,"cart":False,"user":product.user,"category":product.subcategory,"offer":product.offer,"realPrice":product.realPrice})
    

    print(products_list)        
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user = request.user) 
    else:
        notifications = []
    categories = Category.objects.all()
    subCategories = SubCategory.objects.all()
    return render(request,'offers.html',context = {'profile':profile,"products":products_list,"products_shop":products_shop[:4],'chats':all_chats_to,"comments":comments,"username":request.POST.get('name'),"notifications":notifications,"categories":categories,"subs":subCategories})


def offer(request):
    
    product = Product.objects.filter(pk = request.POST.get('pk')).first()
    # print("Quantity",request.POST.get('quantity'))
    if not product.offer:
        product.realPrice = product.price
    product.price = int(request.POST.get('price'))
    if product.realPrice == int(request.POST.get('price')):
        product.offer = False
    else:

        product.offer = True
    product.save()
        
    return JsonResponse({"stock":product.stock,"out":1})

def rating(request):
    profile = userProfile.objects.filter(user = User.objects.filter(username = request.POST.get('username')).first()).first()
    print(profile)
    rating = Rating.objects.filter(Q(user = request.user.username) & Q(doctor = profile.user.username)).first()
    if not rating:
        profile.rating = (profile.rating + int(request.POST.get('rating')) ) / profile.count
        
        profile.count = profile.count +1 
        profile.save()
       
        Rating.objects.create(user = request.user.username,doctor = profile.user.username,rating = int(request.POST.get('rating')))
    else:
        profile.rating = (profile.rating + int(request.POST.get('rating')) ) / profile.count
        
        profile.save()
        
        

    print(request.POST.get('rating'))
    return JsonResponse({"rating":round(profile.rating, 1)})

def increase(request,pk):
    
    
    ct = cart.objects.filter(pk = pk).first()
    ct.quantity = ct.quantity + decimal.Decimal(0.5)
    ct.price = ct.price + (ct.product.price/2)
    ct.save()
    #----------------------------------------------------------------
    return HttpResponseRedirect(reverse('cart'))

def decrease(request,pk):
    
    
    ct = cart.objects.filter(pk = pk).first()
    print(ct.quantity)
    ct.quantity = ct.quantity - decimal.Decimal(0.5)
    print(ct.quantity)
    if ct.quantity > 0:
        ct.price = ct.price - (ct.product.price/2)
        ct.save()
   
    else:
        ct.delete()
    #----------------------------------------------------------------
    return HttpResponseRedirect(reverse('cart'))

import joblib

nb_model = joblib.load('naive.joblib')

def predict_sentiment(comment):
    
    return nb_model.predict([comment])

def comments(request, pk):
    profile = userProfile.objects.filter(user=request.user).first()
    prod = Product.objects.filter(pk=pk).first()
    
    
    comment = request.POST.get('comment')
    
    
    sentiment = predict_sentiment(comment)
    
   
    c = commentUser.objects.create(user=request.user, image=profile.image.url, text=comment, product=prod, sentiment=sentiment)
    c.save()

    return HttpResponseRedirect(reverse('homepage'))