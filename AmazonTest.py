from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.amazon.in/")
time.sleep(3)

# Hover
account_list = driver.find_element(By.ID, "nav-link-accountList")
actions = ActionChains(driver)
actions.move_to_element(account_list).perform()
time.sleep(3)

# Click Your Account (use span - more stable)
driver.find_element(By.XPATH, "//span[text()='Your Account']").click()
time.sleep(5)

print(driver.title)
print(driver.current_url)

# Enter email
email_input = driver.find_element(By.ID, "ap_email")
email_input.send_keys("revardhan@gmail.com")
time.sleep(2)

# Click continue
driver.find_element(By.ID, "continue").click()
time.sleep(3)

# Enter password
driver.find_element(By.ID, "ap_password").send_keys("Maha@$2019")
time.sleep(2)

# Click sign in
driver.find_element(By.ID, "signInSubmit").click()
time.sleep(5)

driver.quit()