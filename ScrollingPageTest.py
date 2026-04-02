
#==================================Scrolling page:==================================

#- With respect to browser not application
#1 - based on the required web element we can scroll
#2 - Initial point to end of the page
#3 - Scroll wherever required
#https://www.countries-ofthe-world.com/flags-of-the-world.html

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()


#1 scroll down page by pixel using jsexecutor

# driver.execute_script("window.scrollBy(0,3000)", "")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved:", value)

#2 scroll down page for the web element

# flag = driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();", flag)
# value = driver.execute_script("return window.pageYOffset;")
# time.sleep(3)
# print("Number of pixels moved:", value)

#3 scroll down till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
time.sleep(3)
print("Number of pixels moved:", value)

#4 scroll to up position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
time.sleep(3)
print("Number of pixels moved:", value)


#==========================Explicit WAIT:======================================

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
wait = WebDriverWait(driver,10)


wait.until(EC.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_useiiir")
print("Username entered")
wait.until(EC.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
print("Password entered")
wait.until(EC.element_to_be_clickable((By.ID,"login-button"))).click()
print("Logged in clicked")
driver.quit()

#==========================Implicit WAIT:======================================

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
#
# driver.get("https://www.saucedemo.com")
# driver.find_element(By.ID, "user-name").send_keys("standard_user")
# print("Username is entered")
# driver.find_element(By.ID, "password").send_keys("secret_sauce")
# print("Password is entered")
# driver.find_element(By.ID, "login-button").click()
# print("logged in")
# time.sleep(3)
# driver.quit()

#=============================Date Picker:=================================


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
time.sleep(3)

driver.switch_to.frame(0)
# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("03/25/2025")

year = "2027"
month = "March"
date = "22"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon == month and yr == year:
        break
    else:
        driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click() #next arrow

dates = driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for element in dates:
    if element.text == date:
        element.click()
        break

#Headless Browser Testing:

#=========================Firefox headless:================================

import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()  # Create an options object
options.add_argument("--headless")  # Add headless mode
options.add_argument("--disable-gpu")  # Disable GPU (good for compatibility)
options.add_argument("window-size=1920,1080")  # Optional, sets browser size

driver = webdriver.Firefox(options=options)
driver.get("http://www.amazon.com")
time.sleep(4)
print(driver.title)
driver.quit()


#======================Chrome headless:================================

# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# # Create options object for headless mode
# options = Options()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("window-size=1920,1080")  # Recommended for headless
# # Pass options while creating the driver
# driver = webdriver.Chrome(options=options)
#
# driver.get("http://www.amazon.com")
# time.sleep(4)
# print("Page Title:", driver.title)
# driver.quit()

