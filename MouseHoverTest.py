#====================== Amazon Hover Example ======================
import email

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
# Launch the Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open Amazon
driver.get("https://www.amazon.in/")
driver.implicitly_wait(10)

# Mouse Hover on  "Hello, Sign in / Account & Lists"
account_list = driver.find_element(By.ID, "nav-link-accountList")

# Create ActionChains object
actions = ActionChains(driver)

# Hover on element
actions.move_to_element(account_list).perform()
driver.implicitly_wait(10)
print(driver.title)
print(driver.current_url)
# Click on "Your Account"
driver.find_element(By.XPATH, "//a[.='Your Account']").click()
driver.implicitly_wait(15)
#driver.find_element(By.XPATH, "//a[contains(text(),'Your Account')]").click()
# time.sleep(3)

driver.find_element(By.CLASS_NAME,"a-box-inner").click()

driver.implicitly_wait(15)

email = driver.find_element(By.ID, "ap_email_login")
email.click()
email.send_keys("revardhan@gmail.com")
driver.implicitly_wait(15)
driver.find_element(By.CLASS_NAME, "a-button-input").click()
# Enter password
driver.find_element(By.NAME, "password").send_keys("Maha@$2019")
driver.implicitly_wait(15)
driver.find_element(By.ID, "signInSubmit").click()
driver.implicitly_wait(15)

# After opening amazon click on main menu
driver.find_element(By.ID, "nav-hamburger-menu").click()
driver.implicitly_wait(15)

# Get menu items (by XPATH)
menu_items = driver.find_elements(By.XPATH, "//div[@id='hmenu-content']")

#print("Total elements:", len(menu_items))

for item in menu_items:
    text = item.text.strip()
 #   if text != " ":
    print(text)
time.sleep(5)
# driver.find_element(By.XPATH,"//a[@class='hmenu-item' and contains(text(),'All Mobile Accessories')]").click()
# driver.implicitly_wait(15)
# for item in menu_items:
#     text = item.text.strip()
#     if "Mobiles,Computers" in text:
#         item.click()

#           driver.implicitly_wait(10)
#         break
driver.find_element(By.XPATH,"//a[contains(normalize-space(),'Mobiles,')]").click()
time.sleep(5)
element = driver.find_element(By.XPATH, "//a[normalize-space()='All Mobile Phones']")
actions = ActionChains(driver)
actions.move_to_element(element).click().perform()
#driver.implicitly_wait(10)

time.sleep(5)
# Close the browser
#driver.quit()
