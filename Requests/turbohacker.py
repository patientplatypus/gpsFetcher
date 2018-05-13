

import requests
from DataClass import *
import json
import os
dirname = os.path.dirname(__file__)

def goTurbo():
    print('in getTurbo...')
    print('...you never go full Turbo')
    print('result of all that Turbo')
    # print(r.text)
    for x in range(0, len(coordArrayData().legStringList)):
        r = requests.get(coordArrayData().legStringList[0])
        savefilename = "/../assets/savecoord" + str(x) + ".txt"
        with open(dirname + savefilename, 'w') as savefile:
            savefile.write(r.text)





## KEEPING HERE FOR FUTURE REFERENCE

## SELENIUM NOT NEEDED !!! THEY HAVE AN API !!!

# import time
# import re
# # from selenium import webdriver
# from selenium.webdriver import Firefox
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.expected_conditions import _find_element

# from DataClass import *


# def goTurbo():
#     print('in getTurbo...')
#     print('...you never go full Turbo')

#     # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
#     # SET UP SELENIUM BROWSER
#     # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#     opts = Options()
#     print("value of coordArrayData().headBool")
#     print(coordArrayData().headBool)
#     if not coordArrayData().headBool:
#         print("inside headless setter")
#         opts.set_headless()
#         assert opts.headless  # operating in headless mode
#     browser = Firefox(options=opts,executable_path="/usr/local/bin/geckodriver")
#     browser.get('https://overpass-turbo.eu/')

#     inputNodes = coordArrayData().legStringList[0]
#     textarea = browser.find_element_by_css_selector('.CodeMirror textarea')
#     textarea.send_keys(Keys.COMMAND + "a")
#     textarea.send_keys(Keys.DELETE)
#     # textarea.send_keys("hello there sailor")
#     textarea.send_keys(inputNodes)
#     WebDriverWait(browser, 1000).until(lambda x: textarea.get_attribute('value').find('node') > -1)
#     # time.sleep(15)
#     # print(textarea.get_attribute('value'))
#     # browser.get('https://www.google.com')
#     browser.find_element_by_css_selector("a[accesskey='1']").click()
#     time.sleep(3)
#     # element = WebDriverWait(browser, 1000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data=t='[title]tabs.data_tt;tabs.data']")));
#     dataarea = browser.find_element_by_css_selector('#dataviewer #data .CodeMirror textarea')
#     print("value of dataarea")
#     print(dataarea.get_attribute('value'))
#     print(dataarea)
#     # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
#     # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
#     # print('value of inputNodes: ')
#     # print(inputNodes)
#     # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
#     # print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
#     # textarea.send_keys(inputNodes)

#     # action = ActionChains(browser)
#     # action.move_to_element_with_offset(textarea, 10, 10)
#     # action.click()
#     # for x in range(1,100):
#     #     action.send_keys(Keys.BACK_SPACE);
#     # action.send_keys("YOLODAWG")

#     # inputbox = browser.find_element_by_tag_name('textarea')
#     # inputbox = browser.find_element_by_xpath("//div[@class='CodeMirror']/div[3]")

#     # print("searching for inputboxInitial")
#     # inputboxInitial = WebDriverWait(browser, 10).until(
#     #     EC.element_to_be_clickable((By.XPATH, "//div[@class='CodeMirror']"))
#     # )
#     # print("found inputboxInitial and clickable")
#     # print(inputboxInitial)

#     # # /div[1]/textarea[1]
#     # print("searching for inputbox")
#     # inputbox = WebDriverWait(browser, 10).until(
#     #     EC.element_to_be_clickable((By.XPATH, "//textarea[1]"))
#     # )
#     # print("found inputbox and clickable")
#     # print(inputbox)


#     # print("1")
#     # action = ActionChains(browser)
#     # print("2")
#     # action.move_to_element_with_offset(inputbox, 100, 100)
#     # print("3")
#     # action.click()
#     # print("4")
#     # action.send_keys(Keys.CONTROL, "a")
#     # print("5")
#     # action.send_keys(inputNodes)
#     # print("6")
#     # action.perform()
#     # print("7")

#     # time.sleep(5)
#     # inputbox.click()
#     # time.sleep(5)
#     # inputbox.send_keys(inputNodes)
