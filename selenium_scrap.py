from time import sleep
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import requests
import shutil
from dotenv import load_dotenv
from pathlib import Path

PATH='./geckodriver'
paper = 25
question = 1
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
USERNAME = os.getenv('username')
PASS = os.getenv('timepass')
driver = webdriver.Firefox(executable_path=PATH)
driver.get("https://www.time4education.com/")
button = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/a')
button.send_keys(Keys.ENTER)
sleep(5)
login = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')
login.send_keys(USERNAME)
password.send_keys(PASS)
button = driver.find_element_by_id('loginbtn')
button.send_keys(Keys.ENTER)
sleep(5)
button = driver.get('https://www.time4education.com/my/aimcats.php')
# button.send_keys(Keys.ENTER)
sleep(5)
result_analysis = driver.find_elements_by_id('resultanalysis')
# result_analysis = [x for x in result_analysis if x.find_element_by_css_selector('a').get_attribute('href')]
ans = list()
for x in result_analysis:
    try:
        x.find_element_by_css_selector('a').get_attribute('href')
        ans.append(x)
    except:
        pass
result_analysis = ans
print(result_analysis[0].find_element_by_css_selector('a').get_attribute('href'))
print(result_analysis.__dir__())
print(len(result_analysis))
for j in range(24, 25):
    ans = []
    res_ans = driver.find_elements_by_id('resultanalysis')
    for x in res_ans:
        try:
            x.find_element_by_css_selector('a').get_attribute('href')
            ans.append(x)
        except:
            pass
    # driver.get(ans[j].find_element_by_css_selector('a').get_attribute('href'))
    window_before = driver.window_handles[0]
    ans[j].click()
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)
    sleep(10)
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    solution_analysis = driver.find_element_by_link_text("Solutions & Analysis")
    driver.get(solution_analysis.get_attribute('href'))
    sleep(5)

    question = 1

    for i in range(1, 35):
        ques = driver.find_element_by_link_text(str(i))
        ques.send_keys(Keys.ENTER)
        sleep(5)
        image = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[6]/div[6]/p/table/tbody/tr[1]/td/img')
        file = open("questions/P"+str(paper)+"Q"+str(question)+".html", "w")
        page = driver.page_source
        file.write(page)
        file.close()
        r = requests.get(image.get_attribute('src'), stream=True)
        if r.status_code == 200:
            with open("answers/P"+str(paper)+"A"+str(question)+".gif", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        question += 1

    select = Select(driver.find_element_by_id('aea1'))
    select.select_by_value("DILR")

    for i in range(1, 33):
        ques = driver.find_element_by_link_text(str(i))
        ques.send_keys(Keys.ENTER)
        sleep(5)
        image = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[6]/div[6]/p/table/tbody/tr[1]/td/img')
        file = open("questions/P"+str(paper)+"Q"+str(question)+".html", "w")
        page = driver.page_source
        file.write(page)
        file.close()
        r = requests.get(image.get_attribute('src'), stream=True)
        if r.status_code == 200:
            with open("answers/P"+str(paper)+"A"+str(question)+".gif", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        question += 1
    select = Select(driver.find_element_by_id('aea1'))
    select.select_by_value("QA")
    for i in range(1, 35):
        ques = driver.find_element_by_link_text(str(i))
        ques.send_keys(Keys.ENTER)
        sleep(5)
        image = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[6]/div[6]/p/table/tbody/tr[1]/td/img')
        file = open("questions/P"+str(paper)+"Q"+str(question)+".html", "w")
        page = driver.page_source
        file.write(page)
        file.close()
        r = requests.get(image.get_attribute('src'), stream=True)
        if r.status_code == 200:
            with open("answers/P"+str(paper)+"A"+str(question)+".gif", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        question += 1
    paper += 1
    driver.get('https://www.time4education.com/my/aimcats.php')
    sleep(5)
