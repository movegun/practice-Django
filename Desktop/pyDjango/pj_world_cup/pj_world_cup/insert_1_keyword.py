from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pj_world_cup.settings")
import django
django.setup()

from world_cupapp.models import All_url

def insert_one_keyword( theme , insert_keyword ):
    
    chrome_driver_path="C:/LDG/PyAdvanced/day06_Crawling/자료실/chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver_path)
    driver.set_window_position(390,90)
    driver.set_window_size(500,700)

    URL2 = 'https://www.google.com/imghp?hl=ko'
    driver.get(URL2)
    
    try:
        el_serch = driver.find_element("name","q")
        el_serch.clear()
        el_serch.send_keys(insert_keyword)
        el_serch.send_keys(Keys.ENTER)
        el_img = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img")
        el_img_url = el_img.get_attribute("src")
        
    except:
        driver.close()
    try:
        if All_url.objects.get(name=insert_keyword):
            print("겹쳐서패스")
            pass
    except All_url.DoesNotExist: # DoesNotExist 가 발생 = DB속에 존재하지 않는다 = 넣어도 된다!
        All_url(theme=theme,name=insert_keyword,url=el_img_url).save()
        print("세이브 한개 완료")
    driver.close()
    
    