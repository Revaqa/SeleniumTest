import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ==============================
# DRIVER SETUP
# ==============================
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
#print(driver.page_source)
print(driver.title)
print(driver.current_url)
wait = WebDriverWait(driver, 10)

# ==============================
# LOGIN PAGE
# ==============================

# Wait for username field to enter
username = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
username.send_keys("standard_user")
wait = WebDriverWait(driver, 5)
# Wait for password field to enter
password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
password.send_keys("secret_sauce")
wait = WebDriverWait(driver, 5)

# Wait for login button clickable
login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
login_btn.click()

# ==============================
# AFTER LOGIN - CLICK PRODUCT AND ADD TO CART
# ==============================

# Wait for Add to Cart button
add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@name,'add-to-cart')]")))
add_to_cart.click()
time.sleep(5)
print(" Product added to cart successfully")
cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-test='shopping-cart-link']")))
cart.click()
print(" Clicked on  cart successfully")
wait = WebDriverWait(driver, 10)

time.sleep(5)

checkout_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='checkout']")))
checkout_btn.click()
time.sleep(5)
#print(current url)
print(driver.title)
print(driver.current_url)
print(" Product checked out from cart successfully")

# ==============================
# CLOSE THE  DRIVER
# ==============================
driver.quit()