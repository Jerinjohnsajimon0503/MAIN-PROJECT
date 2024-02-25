from django.contrib.auth.models import User
from App.models import *
# from models import *
def getCount(request):
    shops = userProfile.objects.filter(is_shopkeeper = True)
    all_shops = []
    for shop in shops:
        try:
            all_shops.append({"name":shop.user.username,"address":shop.shopkeeperAddress,"location":shop.shopkeeperAddress.split(',')[2],"district":shop.shopkeeperAddress.split(',')[1],"image":shop.image,"phone":shop.shopkeeperPhone})
        except:
            pass
    return {
        'count': User.objects.all().count(),
        'balance':userProfile.objects.filter(user = User.objects.filter(username = "admin").first()).first().balance,
        'shops':all_shops,
        'shopkeepersCount':userProfile.objects.filter(is_shopkeeper = True).count(),
        'ordersCount':Order.objects.all().count()
    }