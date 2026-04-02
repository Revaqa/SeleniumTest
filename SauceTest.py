import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(2)
#print(driver.page_source)
print(driver.title)
print(driver.current_url)
user_name = driver.find_element(By.XPATH, "//input[@id ='user-name']")
user_name.click()
driver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(2)
driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.ID, "login-button").click()
time.sleep(6)

driver.find_element(By.XPATH,"//button[contains(@name,'add-to-cart')]").click()
# driver.quit()"
time.sleep(6)