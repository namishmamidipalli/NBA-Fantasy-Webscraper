from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Create a new instance of the web driver
driver = webdriver.Safari()  # Use the appropriate WebDriver (e.g., Chrome)

driver.get("https://www.espn.com")

driver.implicitly_wait(7.0)

# scores = driver.find_element(by=By.CLASS_NAME, value="link-text")
# scores.click()
# title = driver.current_url
# print(title)
driver.quit()
















time.sleep(4.0)
driver.implicitly_wait(5.0)
text_box = driver.find_element(By.NAME, "my-text")
password = driver.find_element(by=By.NAME, value="my-password")

checkboxes = driver.find_element(By.ID, "my-check-2")
checkboxes.click()
radios = driver.find_element(By.ID, "my-radio-2")
radios.click()


submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
text_box.send_keys("hello my nakme is namish")
password.send_keys("Abhish09")
print(title)
print(radios, checkboxes)


# # Navigate to ESPN's website
# driver.get("https://www.espn.com")
# time.sleep(5)  # Wait for 5 seconds

# # Perform scraping actions
# # For example, you can find elements using XPath and extract data
# test = driver.find_element(By.ID, "NBA DRAFT")
# print(test)
# # Close the web driver when you're done
submit_button.click()