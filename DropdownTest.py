#==================================Dropdown:=======================

# https://www.opencart.com/index.php?route=account/register
# Types of Tag names:
# tag name for link, image, text, etc.
# For the dropdown, the tag name is select.
# By using "Select" class we can test.


#Script:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
import time
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(4)
dropdown = driver.find_element(By.XPATH,"//select[@id='country']")
driver.execute_script("arguments[0].scrollIntoView();", dropdown)
time.sleep(2)

#drop_element.select_by_visible_text("Japan")
#drop_element.select_by_value("germany")
#drop_element.select_by_index("9")
#capture all the options in the webpage
drop_element = Select(dropdown)
all_options = drop_element.options
print("Total number of options:", len(all_options))

#print all the options
#for opt in all_options:
#    print(opt.text)

#without in-built methods

for opt in all_options:
    if opt.text == "Germany":
        opt.click()
        break

driver.quit()
