from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import smtplib
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(os.getenv('email'), os.getenv('password'))

SENDER= os.getenv('email')
PASS= os.getenv('password')
RECEIVER= os.getenv('reciever')
PATH='/app/phantomjs'
prev_name1, prev_name2, prev_date = "", "", ""

while True:
    driver = webdriver.PhantomJS(executable_path=PATH)
    driver.get("https://maya.tase.co.il/")
    driver.set_window_size(1920, 1080)
    sleep(5)
    lucky_button = driver.find_element_by_id("searchDesktop")    
    lucky_button.send_keys('קנאביס')
    lucky_button.send_keys(Keys.ENTER)
    sleep(5)    
    name1 = driver.find_element_by_xpath("/html/body/div[2]/div[8]/section/div/div/div/maya-report-actions/div[4]/maya-reports/div[1]/div[2]/div[1]/div[2]/a/h2")
    date = driver.find_element_by_xpath("/html/body/div[2]/div[8]/section/div/div/div/maya-report-actions/div[4]/maya-reports/div[1]/div[3]/div")
    name2 = driver.find_element_by_xpath("/html/body/div[2]/div[8]/section/div/div/div/maya-report-actions/div[4]/maya-reports/div[1]/div[2]/a")
    print(name1.text, name2.text, date.text)

    if prev_name1 != name1.text or prev_name2 != name2.text or prev_date != date.text:
        if name1.text != "איילון":
            msg = "\n New data found "+name1.text
        
            server.sendmail(SENDER, RECIEVER, msg.encode('utf-8'))
            print("Email sent")
    
    prev_name1, prev_name2, prev_date = name1.text, name2.text, date.text
    driver.quit()
    sleep(55)
