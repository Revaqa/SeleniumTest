# =========================Alert:====================================
# Alert is not an web element.
# https://the-internet.herokuapp.com/javascript_alerts

#Script:

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
import time
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()

time.sleep(3)

alert = driver.switch_to.alert
print(alert.text)
time.sleep(3)
alert.send_keys("Goutham")
time.sleep(3)
#alert.accept()
alert.dismiss()
time.sleep(2)


