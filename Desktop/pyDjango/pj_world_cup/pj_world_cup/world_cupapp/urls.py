from django.urls import path
from . import views

urlpatterns = [    
    path('', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('login_ok/', views.login_ok, name='login_ok'),
    path('register/', views.register, name='register'),
    path('register_ok/', views.register_ok, name='register_ok'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('two_imgs/', views.two_imgs, name='two_imgs'),
    path('testpage/', views.testpage, name='testpage'),
    path('winner/', views.winner, name='winner'),
    ]