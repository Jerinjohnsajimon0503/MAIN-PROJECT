from django.urls import path
from . import views 
# from django.conf.urls import url

urlpatterns = [
    
    path('',views.homepage,name = "homepage"),
    path('register/', views.register,name='register' ),
    path('registerShop/', views.registerShop,name='registerShop' ),
    path('login/', views.user_login, name='login'),
    path('checkLogin/', views.checkLogin, name = "checkLogin"),
    path('checkSignup/', views.checkSignup,name = 'checkSignup'),
    path('checkSignupShopkeeper/', views.checkSignup,name = 'checkSignupShopkeeper'),
    path('logout/', views.user_logout,name = 'logout'),
    path('showLogin/', views.show_login,name = 'showLogin'),
    path('showRegister/', views.show_register,name = 'showRegister'),
    # path('productView/', views.productView,name = 'productView'),
    path('addProduct/', views.addProduct,name = 'addProduct'),
    
    ]