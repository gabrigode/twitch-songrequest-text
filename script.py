import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os, json

print ('--------------------------TWITCH-SONGREQUEST-WRITE-----------------------------------------------------')
print ('Opening browser...')
driver = webdriver.Firefox(executable_path=r'PATH WHERE YOU PUT GECKODRIVER.EXE')
driver.get ('YOUR SONG REQUEST URL')

while True:
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    list_name = soup.find('h4')
    print(list_name)
    name = list_name.text.strip()
    name2 = name.replace ("—", "-")
    name2.rstrip()
    print(name2)
    print ('Writing music name on txt file...')
    f = open('music.txt', 'w', encoding='utf-8')
    f.write(name2)
    f.close()
    driver.refresh()
    print ('Refreshing page...')
    time.sleep(5)