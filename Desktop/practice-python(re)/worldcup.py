from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil

try:
    shutil.rmtree(r"c:\chrometemp")  #쿠키 / 캐쉬파일 삭제
except FileNotFoundError:
    pass

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동


option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.implicitly_wait(10)


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import urllib.request
import time

import os

def create_directory(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError:
        print("{} 라는 디렉토리 생성 실패".format(dir))
dir = "브랜드평판탑100"
create_directory(dir)       
        
chrome_driver_path="C:/LDG/PyAdvanced/day06_Crawling/자료실/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

url = 'https://brikorea.com/rk/star2206'
driver.get(url)
el_keywords = driver.find_elements(By.XPATH,"/html/body/div[1]/section/div/div[4]/div[4]/div/div[2]/table/tbody/tr/td[2]")

keywords=[]
for el_keyword in el_keywords:
    keyword = el_keyword.text.strip()
    keywords.append(keyword)


print(keywords)

url = 'https://www.google.com/'
driver.get(url)

count=1
for keyword in keywords:
    
    try:
        el_serch = driver.find_element("name","q")
        el_serch.clear()
        el_serch.send_keys(keyword)
        el_serch.send_keys(Keys.ENTER)        

        el_img = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[10]/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/a/div/div/img")
        el_img_url = el_img.get_attribute("src")


        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        urllib.request.urlretrieve(el_img_url,f"{dir}/"+f"{count}"+f"{keyword}"+".jpg")
        count=count+1
    except:
        pass
          

    
#     url = 'https://www.google.com/'
#     driver.get(url)



    
#     el_serch = driver.find_element("name","q")
#     el_serch.send_keys(keyword)
#     el_serch.send_keys(Keys.ENTER)
        
#     el_img = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[10]/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/a/div/div/img")
#     el_img_url = el_img.get_attribute("src")
    
#     opener=urllib.request.build_opener()
#     opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
#     urllib.request.install_opener(opener)
    
#     urllib.request.urlretrieve(el_img_url,f"{dir}/"+f"{keyword}"+".jpg")        
#     time.sleep(1)
#     print("끝")
    


# # driver.get(url)

# # el_img = driver.find_element(By.XPATH, "/html/body/div[7]/div/div[10]/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div/div[1]/a/div/div/img")
# # el_img_url = el_img.get_attribute("src")

# # opener=urllib.request.build_opener()
# # opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
# # urllib.request.install_opener(opener)


# # import os

# # def create_directory(dir):
# #     try:
# #         if not os.path.exists(dir):
# #             os.makedirs(dir)
# #     except OSError:
# #         print("{} 라는 디렉토리 생성 실패".format(dir))

# # create_directory("down")


# # urllib.request.urlretrieve(el_img_url,"down/"+"손석구"+".jpg")

# # print("el_img_url",el_img_url)