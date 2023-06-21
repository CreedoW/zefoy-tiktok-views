#IMPORTS
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

#OPTIONS
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#DRIVER SETTINGS
os.environ['PATH'] += r".\chromedriver.exe"
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://zefoy.com/")

#VARIABLES&STARTING PRINTS
print("VIDEO LINK:")
linktiktok = input()

print("How many loops:")
loopss = input()

print("COMPLETE CAPTCHA IN BROWSER")


#SCRAP&AUTOMATION
captcha = wait(driver, 20).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'mb-1.mt-2')))
#CLEAR
os.system('cls' if os.name == 'nt' else "printf '\033c'") #-- CLEARING CMD/PS BEFORE PRINTS
#SCRAP&AUTOMATION
views = wait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn.btn-primary.rounded-0.menu4'))).click()
links = wait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="sid4"]/div/form/div/input'))).send_keys(linktiktok)
search = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="sid4"]/div/form/div/div/button'))).click()
selectvideo = wait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-dark'))).click()

#RESULT1
print("VIEWS SENT SUCCESSFULLY !")

#SLEEP UNTILL READY FOR NEXT VIEWS
time.sleep(240)

#LOOPING
for i in range(loopss):
  search1 = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="sid4"]/div/form/div/div/button'))).click()
  selectvideo1 = wait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-dark'))).click()
  print("VIEWS SENT SUCCESSFULLY !")
  time.sleep(240)

#ONCE FINISHED THE PROCESS THAT THING WILL MAKE THE BROWSER GET CLOSED !
driver.quit()
print("test")
