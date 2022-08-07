from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
import time
    
chrome_driver_path="C:/LDG/PyAdvanced/day06_Crawling/자료실/chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(chrome_driver_path,options=options)


import os
def create_directory(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError:
        print("{} 라는 디렉토리 생성 실패".format(dir))
dir = "브랜드평판탑100"
create_directory(dir)       
        

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
fail_keywords=[]


folder_path = 'c:/Users/Kosmo/Desktop/practice-python/브랜드평판탑100'
def get_files_count():
	dirListing = os.listdir(folder_path)
	return len(dirListing)


def start(listname):
    global driver  
    for keyword in listname:       
        try:
            if get_files_count()==100:                
                return  
            el_serch = driver.find_element("name","q")
            el_serch.clear()
            el_serch.send_keys(keyword)
            el_serch.send_keys(Keys.ENTER)        

            el_img = driver.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img")
            el_img_url = el_img.get_attribute("src")


            opener=urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            print(f"{keyword}의 url :",el_img_url)
            

            urllib.request.urlretrieve(el_img_url,f"{dir}/"+f"{keyword}"+".jpg")
            keywords.remove(keyword)                      
        # except NoSuchElementException:
        #     pass           
        except :
            fail_keywords.append(keyword)                     
            driver.close()            
            driver = webdriver.Chrome(chrome_driver_path,options=options)                     
            driver.get(URL2)
            print("예외 발생 후 keywords",keywords)            
            start(keywords.copy())        
            
start(keywords.copy())



print("끝")