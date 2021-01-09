from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Running Headless Browser
options=Options()
options.headless=True
browser=webdriver.Firefox(options=options, executable_path=r'C:\Users\anvu0\Documents\tradelog\geckodriver.exe')

#Running Non Headless Browser
#browser=webdriver.Firefox(executable_path=r'C:\Users\anvu0\Documents\tradelog\geckodriver.exe')

#Open First tab
browser.get('https://swingtradebot.com/users/sign_in')

time.sleep(1)

#Find page 
URL='https://swingtradebot.com/scans/top-gainers?selected_date='
currentDate=datetime.now()
Date=str(currentDate.day)
Month=str(currentDate.month)
Year=str(currentDate.year)
getURL=URL+Month+'%2F'+Date+'%2F'+Year
script="window.open('" + getURL + "','new_window')"
browser.execute_script(script)

time.sleep(2)

#switch to active tab
browser.switch_to.window(browser.window_handles[1])

time.sleep(1)

#find csv download
opBoxes=browser.find_elements_by_css_selector('button.btn.btn-sm.btn-primary.mt-1')
print(len(opBoxes))
csv_box=opBoxes[1].click()


#actions=ActionChains(browser)
#actions.send_keys(Keys.TAB*6)
#actions.perform()
#time.sleep(10)
#print(len(opBoxes))

time.sleep(2)

#browser.save_screenshot('screenshot.png')

browser.quit()
