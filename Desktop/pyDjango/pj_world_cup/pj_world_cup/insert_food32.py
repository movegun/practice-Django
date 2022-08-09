from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pj_world_cup.settings")
import django
django.setup()

from world_cupapp.models import All_url




def read_text():
    file = open("C:/Users/Kosmo/Desktop/채소 32강.txt", "r" , encoding='UTF8')
    dict = {}
    for line in file:
        one_line = line.strip()
        print(one_line)
        
        name_and_url = one_line.split(" ")
        print(name_and_url)
        dict[name_and_url[0]]=name_and_url[1]
    
    for key,value in dict.items():
        All_url(theme='vegetable',name=key,url=value).save()
        
        #vegetable
        
read_text()