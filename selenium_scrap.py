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
PATH='./phantomjs'
prev_name1, prev_name2, prev_date, prev_name3, prev_name4, prev_date1 = "", "", "", "", "", ""

while True:
    driver = webdriver.PhantomJS(executable_path=PATH)
    driver.get("https://maya.tase.co.il/")
    driver.set_window_size(1920, 1080)
    sleep(5)
    lucky_button = driver.find_element_by_id("searchDesktop")    
    lucky_button.send_keys('קנאביס')
    lucky_button = driver.find_element_by_xpath('/html/body/div[2]/nav/div/div[2]/form/button')
    lucky_button.send_keys(Keys.ENTER)
    sleep(5)    
    name1 = driver.find_element_by_xpath("/html/body/div[2]/div[8]/section/div/div/div/maya-report-actions/div[4]/maya-reports/div[1]/div[2]/div[1]/div[2]/a/h2")
    date = driver.find_element_by_xpath("/html/body/div[2]/div[8]/section/div/div/div/maya-report-actions/div[4]/maya-reports/div[1]/div[3]/div")
    name2 = driver.find_element_by_xpath("/html/body/div[2]/div[8]/section/div/div/div/maya-report-actions/div[4]/maya-reports/div[1]/div[2]/a")
    print(name1.text, name2.text, date.text)

    if prev_name1 != name1.text or prev_name2 != name2.text or prev_date != date.text:
        if name1.text != "איילון":
            msg = "\n New data found "+name1.text
            message = 'Subject: {}\n\n{}'.format("Maya Update", msg)
            server.sendmail(SENDER, RECEIVER, message.encode('utf-8'))
            print("Email sent")
    prev_name1, prev_name2, prev_date = name1.text, name2.text, date.text    
    driver.quit()
    driver = webdriver.PhantomJS(executable_path=PATH)
    driver.get("https://maya.tase.co.il/")
    driver.set_window_size(1920, 1080)
    sleep(5)
    lucky_button = driver.find_element_by_id("searchDesktop")
    lucky_button.send_keys('מריחואנה')
    lucky_button = driver.find_element_by_xpath('/html/body/div[2]/nav/div/div[2]/form/button')
    lucky_button.send_keys(Keys.ENTER)
    sleep(5)

    name3, date1, name4 = name1, date, name2
    try:
        name3 = driver.find_element_by_xpath("/html/body/div[2]/div[8]/section/div/div/div/maya-report-actions/div[4]/maya-reports/div[1]/div[2]/div[1]/div[2]/a/h2")
        date1 = driver.find_element_by_xpath("/html/body/div[2]/div[8]/section/div/div/div/maya-report-actions/div[4]/maya-reports/div[1]/div[3]/div")
        name4 = driver.find_element_by_xpath("/html/body/div[2]/div[8]/section/div/div/div/maya-report-actions/div[4]/maya-reports/div[1]/div[2]/a")
    
        print(name3.text, name4.text, date1.text, name3.get_attribute)

        if prev_name3 != name3.text or prev_name4 != name4.text or prev_date1 != date1.text or prev_name1 != name3.text or prev_name2 != name4.text or prev_date != date1.text:
            if name3.text != "איילון":
                msg = "\n New data found "+name3.text
                message = 'Subject: {}\n\n{}'.format("Maya Update", msg)
                server.sendmail(SENDER, RECEIVER, message.encode('utf-8'))
                print("Email sent")


    
        prev_name3, prev_name4, prev_date1 = name3.text, name4.text, date1.text
    except:
        print("No results for מריחואנה")
    
    driver.quit()
    sleep(55)
