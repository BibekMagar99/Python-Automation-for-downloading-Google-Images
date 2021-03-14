from selenium import webdriver
#import webdriver of selenium
from selenium.webdriver.common.keys import Keys
import time
import pyautogui 
#Opens up web driver and goes to Google Images
driver = webdriver.Edge('C:/edgedriver_win64/msedgedriver.exe')
#webdriver lai access gareko
driver.get('https://www.bing.com/?scope=images&nr=1&FORM=NOFORM')
box = driver.find_element_by_xpath('//*[@id="sb_form_q"]')
box.send_keys('"Defaced website"')
box.send_keys(Keys.ENTER)
box = driver.find_element_by_xpath('//*[@id="b-scopeListItem-images"]/a')
box.send_keys(Keys.ENTER)
time.sleep(1)
box = driver.find_element_by_xpath('//*[@id="mmComponent_images_2"]/ul[1]/li[1]/div/div[2]/div/div/ul/li/a')
box.send_keys(Keys.ENTER)
time.sleep(3)
for i in range (1,50):
    pyautogui.moveTo(431, 485)
    time.sleep(2)
    pyautogui.click(button='right')
    time.sleep(2)
    pyautogui.click(x=538, y=551)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(2)
    pyautogui.write('C:/Users/bibek/Desktop/python projects/Google Images/Images Here')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=457, y=666)
    time.sleep(2)
    pyautogui.write(str(i))
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=835, y=530)
    time.sleep(2)