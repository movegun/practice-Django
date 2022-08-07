from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path="C:/LDG/PyAdvanced/day06_Crawling/자료실/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(chrome_driver_path,options=options)

# URL = 'https://brikorea.com/rk/star2206'

# driver.get(url=URL)

# el_keywords = driver.find_elements(By.XPATH,"/html/body/div[1]/section/div/div[4]/div[4]/div/div[2]/table/tbody/tr[]<5/td[2]")

# keywords=[]
# for el_keyword in el_keywords:
#     keyword = el_keyword.text.strip()
#     keywords.append(keyword)    
    

# print(keywords)
# print(len(keywords))
# driver.close()

# driver = webdriver.Chrome(chrome_driver_path,options=options)
driver = webdriver.Chrome(chrome_driver_path)
URL2 = 'https://www.google.com/imghp?hl=ko'
driver.get(URL2)
fail_keywords=[]
keywords=['손석구','강호동','아이유','싸이','유재석','방탄소년단']
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
        if len(dicts)>64:
            break
    except:
        driver.close()            
        driver = webdriver.Chrome(chrome_driver_path,options=options)                     
        driver.get(URL2)


driver.close()
print(dicts)

from world_cupapp.models import Brand_member

for key in dicts:    
    bm=Brand_member(name=key,url=dicts[key])
    if Brand_member.objects.get(name=key):
        print("겹쳐서 패스")
        pass
    else:
        bm.save()
print(Brand_member.objects.all())
# def start(listname):
#     global driver
#     for keyword in listname:            
#         try:      
#             el_serch = driver.find_element("name","q")
#             el_serch.clear()
#             el_serch.send_keys(keyword)
#             el_serch.send_keys(Keys.ENTER)        

#             el_img = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img")
#             el_img_url = el_img.get_attribute("src")
            
#             dicts[keyword]=el_img_url
#             print(dicts)
                        
#             keywords.remove(keyword)            
                                  
#         # except NoSuchElementException:
#         #     pass           
#         except :
#             fail_keywords.append(keyword)                     
#             driver.close()            
#             # driver = webdriver.Chrome(chrome_driver_path,options=options)    
#             driver = webdriver.Chrome(chrome_driver_path)                 
#             driver.get(URL2)
#             print("예외 발생 후 keywords",keywords)
#             start(keywords.copy())
            
# start(keywords.copy())
# driver.close()





# from .models import Brand_member

# row = Brand_member(name=)