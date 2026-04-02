# ================================Check box:=================================

# Select a single check box, multi check box in the DOM Page.
# https://testautomationpractice.blogspot.com/


#===============================Method-1:=============================================
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver.get("https://testautomationpractice.blogspot.com/?m=1")
# driver.maximize_window()
# time.sleep(2)
#
# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='sunday']")))
# driver.execute_script("arguments[0].scrollIntoView();", element)
# element.click()
#
# a= driver.find_element(By.XPATH,"//input[@id='monday']")
# a.click()
# c = driver.find_element(By.XPATH,"//input[@id='tuesday']")
# c.click()
# d = driver.find_element(By.XPATH,"//input[@id='wednesday']")
# d.click()
# e = driver.find_element(By.XPATH,"//input[@id='thursday']")
# e.click()
# f = driver.find_element(By.XPATH,"//input[@id='friday']")
# f.click()
# g = driver.find_element(By.XPATH,"//input[@id='saturday']")
# g.click()
# time.sleep(5)
# driver.quit()

#=======================================Method 2:==========================================

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
import time
driver.get("https://testautomationpractice.blogspot.com/?m=1")
driver.maximize_window()
time.sleep(2)
check_boxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
#//input[@type='checkbox' and contains(@id,'day')]
print(len(check_boxes))
#approach 1
#for i in range(len(check_boxes)):
#   check_boxes[i].click()
#approach 2
#for checkbox in check_boxes:
#   checkbox.click()
#Multi select
for checkbox in check_boxes:
    weekname = checkbox.get_attribute('id')
    if weekname =='monday'or weekname == 'sunday':
        # ✅ SCROLL HERE (before click)
        driver.execute_script("arguments[0].scrollIntoView();", checkbox)
        time.sleep(3)
        checkbox.click()

#clearing all the text boxes
# for checkbox in check_boxes:
#     if checkbox.is_selected():
#         checkbox.click()
driver.quit()

