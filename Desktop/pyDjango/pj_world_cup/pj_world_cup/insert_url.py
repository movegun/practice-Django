from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pj_world_cup.settings")
import django
django.setup()

from world_cupapp.models import Urls


def return_dicts():
    chrome_driver_path="C:/LDG/PyAdvanced/day06_Crawling/자료실/chromedriver.exe"
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(chrome_driver_path,options=options)
    
    
    URL = 'https://brikorea.com/rk/star2206'

    driver.get(url=URL)

    el_keywords = driver.find_elements(By.XPATH,"/html/body/div[1]/section/div/div[4]/div[4]/div/div[2]/table/tbody/tr/td[2]")

    keywords=[]
    for el_keyword in el_keywords:
        keyword = el_keyword.text.strip()
        keywords.append(keyword)    


    print(keywords)
    print(len(keywords))
    driver.close()
    
    driver = webdriver.Chrome(chrome_driver_path,options=options)
    
    URL2 = 'https://www.google.com/imghp?hl=ko'
    driver.get(URL2)    
    dicts={}

    for key in keywords:
        el_serch = driver.find_element("name","q")
        el_serch.clear()
        el_serch.send_keys(key)
        el_serch.send_keys(Keys.ENTER)
        el_img = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img")
        el_img_url = el_img.get_attribute("src")
        
        dicts[key]=el_img_url
        if len(dicts)>64:
            break
                
        
    driver.close()

    return dicts

if __name__=='__main__':    
    url_dict = return_dicts()
    for name, url in url_dict.items():
        if len(Urls.objects.all())>64:
            break
        if Urls.objects.get(name=name):
            print("겹처서패스")
            pass
        else:
            Urls(name=name,url=url).save()
            print("세이브 한개 완료")    
    
    print("URLS 모델 총 row 갯수:",len(Urls.objects.all()))
