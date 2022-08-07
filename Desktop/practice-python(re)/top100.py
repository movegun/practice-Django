from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess

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

# chrome_driver_path="C:/LDG/PyAdvanced/day06_Crawling/자료실/chromedriver.exe"
# options = webdriver.ChromeOptions()
# options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# driver = webdriver.Chrome(chrome_driver_path,options=options)

import os
def create_directory(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
    except OSError:
        print("{} 라는 디렉토리 생성 실패".format(dir))
dir = "남자아이돌100"
# create_directory(dir)

URL='https://www.piku.co.kr/w/rank/8b7pAF'

driver.get(url=URL)

# el_serch = driver.find_element("name","q")
# el_serch.clear()
# el_serch.send_keys('피쿠')
# el_serch.send_keys(Keys.ENTER)

# el_combobox = driver.find_element(By.CLASS_NAME,"LC20lb.MBeuO.DKV0Md")
# el_combobox.click()

# el_combobox = driver.find_element("name","DataTables_Table_0_length")
# el_combobox.click()
# time.sleep(1)
# el_combobox.send_keys(Keys.ARROW_DOWN)
# el_combobox.send_keys(Keys.ARROW_DOWN)
# el_combobox.send_keys(Keys.ARROW_DOWN)
# time.sleep(1)
# el_combobox.send_keys(Keys.ENTER)

# el_names = driver.find_elements(By.XPATH,'/html/body/div[2]/div/div[4]/div/div/div/div[2]/div[1]/div/table/tbody/tr/td[3]')
# names=[]

# for name in el_names:
#     print(name.text)
    
# el_imgs = driver.find_elements(By.CLASS_NAME,'.thumb')

# i=1
# for el_img in el_imgs:
#     img=el_img.get_attribute("src")
#     print(img)
#     opener=urllib.request.build_opener()
#     opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
#     urllib.request.install_opener(opener)

#     urllib.request.urlretrieve(img,"103"+f"{i}"+".jpg")
#     i=i+1

    
