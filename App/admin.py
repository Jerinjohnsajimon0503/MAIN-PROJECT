from django.contrib import admin
from .models import *
class Prod(admin.ModelAdmin):
    exclude = ('dosage', 'activeIngredient', 'route', 'manufacturerName', 'manufacturerAddress', 'manufacturerCountry', 'manufacturerContactNumber')
# Register your models here.
admin.site.register(ShopKeeper)
admin.site.register(userProfile)
admin.site.register(Product,Prod)



