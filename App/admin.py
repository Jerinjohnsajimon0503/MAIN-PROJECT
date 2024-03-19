from django.contrib import admin
from .models import userProfile,Product,cart,Order,Chat,Comment,Notification,Category,SubCategory,Payment,ShopKeeper,commentUser
class Prod(admin.ModelAdmin):
    exclude = ('dosage', 'activeIngredient', 'route', 'manufacturerName', 'manufacturerAddress', 'manufacturerCountry', 'manufacturerContactNumber')
# Register your models here.
admin.site.register(ShopKeeper)
admin.site.register(userProfile)
admin.site.register(Product,Prod)
# admin.site.register(cart)
admin.site.register(Order)
admin.site.register(Chat)
admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Payment)
admin.site.register(commentUser)