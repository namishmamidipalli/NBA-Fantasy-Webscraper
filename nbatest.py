from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pywebcopy

# # Create a new instance of the web driver
driver = webdriver.Safari()  # Use the appropriate WebDriver (e.g., Chrome)


driver.get('https://www.espn.com/')
driver.maximize_window()
driver.set_window_size(1500, 900)
time.sleep(3)

##Open Initial Log In Location
search_box = driver.find_element(by=By.ID, value='global-user-trigger')
search_box.click()
time.sleep(2)
print('Open Log In Tab')
# Click on the Log In location
nextbox = driver.find_element(by=By.XPATH, value="//a[@data-affiliatename='espn']")
print(nextbox.text)
nextbox.click()
print('Click Login')
#Switch to iFrame to enter log in credentials
driver.implicitly_wait(7.0)
time.sleep(3.0)


driver.switch_to.frame("oneid-iframe")

# test = driver.find_element(by=By.ID, value="Title")
# print(test.text)
# username = driver.find_element(by=By.XPATH, value="//input[@placeholder='Username or Email Address']")
actual_link = driver.find_element(by=By.LINK_TEXT, value="Looking for username login?")
print(actual_link.text)
actual_link.click()

username = driver.find_element(by=By.ID, value="InputLoginValue")

# print('Switching to iFrame')
# # ##Submit Username and Password
time.sleep(2)
username.send_keys('namishkmami@gmail.com')
# password = driver.find_element_by_xpath("//input[@placeholder='Password (case sensitive)']")
password = driver.find_element(by=By.ID, value="InputPassword")
password.send_keys('Abhish09')
time.sleep(2)
# print('Logging In')
# # ##Submit credentials
submit_button = driver.find_element(by=By.ID, value="BtnSubmit")
submit_button.click()
time.sleep(10.0)
# ##Open Link Page
# time.sleep(4.0)
# fantasy = driver.find_element(by=By.ID, value='fantasy__footer')
# print(fantasy.text)
driver.switch_to.default_content()
# search_box = driver.find_element(by=By.ID, value='global-user-trigger')
# search_box.click()

# fantasy_link = driver.find_element(by=By.NAME, value="&lpos=sitenavcustom+sitenav_fantasy")
# fantasy_link.click()
# driver.implicitly_wait(4.0)
# element = driver.find_element(by=By.XPATH, value="//a[@href='https://fantasy.espn.com/basketball/team?leagueId=1416211800&teamId=2&seasonId=2024' and @name='&lpos=sitenavcustom+fantasy+team_namish']")
# element.click()
# my_team = driver.find_element(by=By.NAME, value="&lpos=fp:fantasy:fba:1:team")
# print(my_team.text)
# my_team.click()
search_box = driver.find_element(by=By.ID, value='global-user-trigger')
search_box.click()
print('Going to Fantasy Link')
##Selecting Fantasy League
time.sleep(2)
leaguego = driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Team Namish')
leaguego.click()

driver.implicitly_wait(4.0)
time.sleep(4.0)
# print(fantasy.text)
print('Going to Fantasy Link')
# # ##Selecting Fantasy League
# # time.sleep(2)
# leaguego = driver.find_element_by_partial_link_text('Team Namish')
# leaguego.click()
# print('Entering League')
# site = driver.page_source













# # time.sleep(4.0)
# # driver.implicitly_wait(5.0)
# # text_box = driver.find_element(By.NAME, "my-text")
# # password = driver.find_element(by=By.NAME, value="my-password")

# # checkboxes = driver.find_element(By.ID, "my-check-2")
# # checkboxes.click()
# # radios = driver.find_element(By.ID, "my-radio-2")
# # radios.click()


# # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
# # text_box.send_keys("hello my nakme is namish")
# # password.send_keys("Abhish09")
# # print(title)
# # print(radios, checkboxes)


# # # # Navigate to ESPN's website
# # # driver.get("https://www.espn.com")
# # # time.sleep(5)  # Wait for 5 seconds

# # # # Perform scraping actions
# # # # For example, you can find elements using XPath and extract data
# # # test = driver.find_element(By.ID, "NBA DRAFT")
# # # print(test)
# # # # Close the web driver when you're done
# # submit_button.click()