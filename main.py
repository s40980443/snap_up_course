

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
'''
高科選課系統
這是一個一直幫你刷新 有沒有空缺的加退選

在username輸入你的高科帳號
password 輸入你的密碼
jiangongList_1grade 輸入選課代號
'''
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.HEADER}高科選課系統{bcolors.ENDC} \n\n"
      "這是一個一直幫你刷新 有沒有空缺的加退選\n"
      "**********************************\n")



username = input("輸入你的高科帳號:")

password = input("輸入你的高科密碼:")
x = input(f"\n"
          f"{bcolors.FAIL}注意每隔課程中隔一隔半行空格{bcolors.ENDC}\n"
          f"課程代號有需要查詢的話請到     {bcolors.WARNING}校務系統 -> 查詢 -> 課程資訊{bcolors.ENDC}\n"
          f"輸入你的課程代號:\n")

course = x.split(' ')
jiangongList_1grade = []
jiangongList_1grade = course




chromedriver = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('https://aais5.nkust.edu.tw/selcrs_std/AddSelect/AddSelectPage')
driver.set_window_size(1024, 768)





def Login():
    username_search = driver.find_element_by_xpath('//*[@id="UserAccount"]')
    username_search.send_keys(username)
    print("username:" + username)
    driver.implicitly_wait(10)
    password_search = driver.find_element_by_xpath('//*[@id="Password"]')
    password_search.send_keys(password)
    print("password" + password)
    driver.implicitly_wait(10)
    login_in = driver.find_element_by_xpath('//*[@id="Login"]')
    login_in.click()
    print("login 成功")

def select_course():
    add_btn = driver.find_element(By.XPATH, '/html/body/div/aside[1]/div/nav/ul/li[1]/a/div')
    add_btn.click()
    driver.implicitly_wait(10)
    add_course = driver.find_element(By.XPATH, '/html/body/div/aside[1]/div/nav/ul/li[1]/ul/li[1]/a/div')
    add_course.click()
    driver.implicitly_wait(10)






Login()
time.sleep(3)

select_course()
time.sleep(3)

count = 0
while 1:
    time.sleep(1)
    course_Number = driver.find_element(By.XPATH, '//*[@id="scr_selcode"]')

    course_Number.send_keys(jiangongList_1grade[count])
    print("課程代碼" + jiangongList_1grade[count])
    count += 1
    time.sleep(1)

    search = driver.find_element(By.XPATH, '//*[@id="courseSearch"]')
    search.click()
    time.sleep(1)
    add = driver.find_element(By.CLASS_NAME, 'btn_addcrs')
    add.click()
    time.sleep(8)
    if count == len(jiangongList_1grade):
        count = 0

driver.quit()








