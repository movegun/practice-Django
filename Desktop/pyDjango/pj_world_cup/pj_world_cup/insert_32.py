from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pj_world_cup.settings")
import django
django.setup()

from world_cupapp.models import All_url



def return_dicts():
    chrome_driver_path="C:/LDG/PyAdvanced/day06_Crawling/자료실/chromedriver.exe"
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    # driver = webdriver.Chrome(chrome_driver_path,options=options)
    # URL = 'https://brikorea.com/rk/star2206'    
    # driver.get(url=URL)
    
    # el_keywords = driver.find_elements(By.XPATH,"/html/body/div[1]/section/div/div[4]/div[4]/div/div[2]/table/tbody/tr/td[2]")
     
    # keywords=[]
    # for el_keyword in el_keywords:
    #     keyword = el_keyword.text.strip()
    #     keywords.append(keyword)
    #     if len(keywords)==32:
    #         break
    # print(keywords)    
    # driver.close()

    # keywords=["이상해씨","파이리","리자드","리자몽","꼬부기","거북왕","단데기","버터플","메가독침붕",
    #       "피죤","아보크","피카츄","식스테일","뚜벅쵸","콘팡","디그다","나옹이","고라파덕","성원숭","슈륙챙이","윤겔라",
    #       "알통몬","우츠동","꼬마돌","야도란","파오리","질퍽이","롱스톤","찌리리공","홍수몬","내루미","또가스"]
    
    keywords= ['포메라니안','골든리트리버','시츄','시베리안 허스키','진돗개','웰시코기','말라뮤트','토이푸들','비숑프리제',
               '말티즈','래브라도 리트리버','시바견','보더콜리','스피츠','파피용','저먼 셰퍼드','닥스훈트','요크셔테리어',
               '프렌치불독','셔틀랜드 쉽독','치와와','비글','그레이트피레니즈','차우차우','퍼그','롯트와일러','미니어쳐핀셔',
               '슈나우져','코카스파니엘','불독','보스턴테리어','샤페이'
               ]
    driver = webdriver.Chrome(chrome_driver_path,options=options)    
    URL2 = 'https://www.google.com/imghp?hl=ko'
    driver.get(URL2)
    dicts={}
    for key in keywords:
        try:
            el_serch = driver.find_element("name","q")
            el_serch.clear()
            el_serch.send_keys(key)
            el_serch.send_keys(Keys.ENTER)
            el_img = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img")
            el_img_url = el_img.get_attribute("src")
            
            dicts[key]=el_img_url
            if len(dicts)==32:
                break
        except:
            driver.close()
            driver = webdriver.Chrome(chrome_driver_path,options=options)
            driver.get(URL2)
            pass
    driver.close()
    return dicts

if __name__=='__main__':
    url_dict = return_dicts()
    for name, url in url_dict.items():
        
        # if len(All_url.objects.all())==32:
        #     break
        try:
            if All_url.objects.get(name=name):
                print("겹쳐서패스")
                pass
            else:
                All_url(theme='dog',name=name,url=url).save()
                print("세이브 한개 완료")
        except:
            All_url(theme='dog',name=name,url=url).save()
            print("세이브 한개 완료")
    
    
    print("All_url 모델 총 row 갯수:",len(All_url.objects.all()))