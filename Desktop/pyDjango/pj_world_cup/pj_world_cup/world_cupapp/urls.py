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
    path('modal/<str:selected_theme>/', views.modal, name='modal'),
    path('test/', views.test, name='test'),
    path('<str:selected_theme>/<int:selected_rounds>', views.play, name='play'),
    path('winner/<str:selected_theme>/<str:selected_name>', views.winner, name='winner'),
    path('ranking/<str:selected_theme>', views.ranking, name='ranking'),
    path('new_keyword/', views.new_keyword, name='new_keyword'),
    path('insert/<str:selected_theme>/<str:insert_name>', views.insert_new_keyword, name='insert_new_keyword'),
    path('admin_check/', views.admin_check, name='admin_check'),
    path('ehdrjs/', views.ehdrjs, name='ehdrjs'),
    ]