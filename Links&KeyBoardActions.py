# ================================Links:=========================

# - Internal
# - By clicking on the link, it will be navigate on the same page
# - External
# - By clicking on the link, it will be navigate to another web page.
# https://demo.nopcommerce.com/
# <a> - anchor tag - represent the link
# href - hyperlink reference
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
links = driver.find_elements(By.XPATH,"//a")
print("Total no.of links:",len(links))
driver.quit()


for link in links:
    print(link.text)

#=============Broken :======================================================
# - By clicking on the link, no target page accessed.
# - Doesn't have any target page.
# - Greater than or equal to 400 error
# - We need requests package to test it (API)
#http://www.deadlinkcity.com/


#==================================Keyboard:============================
# Box is small, then we will call it as "input box"
# Box is very larger, then we call it as "text area"
# https://text-compare.com/

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
driver.maximize_window()

input1 = driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")
input1.send_keys("Welcome to the selenium")

act = ActionChains(driver)
# ControlA
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
# Control C
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
time.sleep(2)
# TAB
act.send_keys(Keys.TAB).perform()
#Control V
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(3)
driver.quit()
