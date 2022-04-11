from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\webdriver\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()

email_box=driver.find_element(By.XPATH,"//input[@id='Email']")
email_box.clear()
email_box.send_keys("deepma@gmail.com")
print("RESULT:",email_box.text)# THIS WILL NOT RETUEN ANYTHING
print("get_attrinute()",email_box.get_attribute('value'))#deepma23@gmail.com

