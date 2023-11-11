from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pywebcopy
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pandas as pd

# # Create a new instance of the web driver
driver = webdriver.Safari()  # Use the appropriate WebDriver (e.g., Chrome)


driver.get('https://www.espn.com/')
driver.maximize_window()
driver.set_window_size(1500, 900)
time.sleep(8)

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

actual_link = driver.find_element(by=By.LINK_TEXT, value="Looking for username login?")
print(actual_link.text)
actual_link.click()

username = driver.find_element(by=By.ID, value="InputLoginValue")


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

driver.switch_to.default_content()


search_box = driver.find_element(by=By.ID, value='global-user-trigger')
search_box.click()
##Selecting Fantasy League
time.sleep(2)
leaguego = driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Namish')
leaguego.click()

driver.implicitly_wait(4.0)
time.sleep(4.0)
print('Going to Fantasy Link')



time.sleep(4.0)
driver.switch_to.default_content()

calendar = driver.find_element(by=By.XPATH, value="//button[@aria-label='Calendar' and @class='DateCarousel__MonthTrigger']")
calendar.click()
driver.implicitly_wait(4.0)
date = driver.find_element(by=By.XPATH, value="//li[@class='MonthContainer__Day MonthContainer__Day--noEvent' and text()='12']")
date.click()
# calendar.click()

time.sleep(4.0)
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')


# bench = soup.findAll('td', {'class': 'Table__TD Table__TD--fixed-width', 'style': 'width: 60px;'})
pos = soup.findAll('div', attrs={'class': 'jsx-2810852873 table--cell'})
player_info = soup.findAll('div', attrs={"class": "jsx-1811044066 player-column__bio"})
matchups = soup.findAll('div', attrs={"class": "jsx-2810852873 table--cell opp ml4"})

# players = soup.findAll('td', {'class': 'Table__TD Table__TD--fixed-width', 'style': 'width: 228px;'})
# borderplayer = soup.findAll('td', {'class': 'Table__TR Table__TR--lg Table__odd Table__border-row'})
players = soup.findAll('div', attrs={'class': 'jsx-1811044066 player-column__athlete flex'})

playing_but_bench = []

for p, player, opps in zip(pos, players, matchups):
    print(player.text, "opponent is", opps.text, "pos is ", p.text)
    if "Bench" in p.text and opps.text != "--":
        playing_but_bench.append(player)

for player in playing_but_bench:
    print(player.text, "is playing but is on your bench!")

for player in playing_but_bench:
    print(player)

# for player, opps in zip(players, matchups):
#     print(player.text, "opponent is", opps.text)
#     if "Bench" in player.text and opps.text != "--":
#         print(player.text + " has a game but is on the bench.")

# bench_players_with_games = []
# for player, benchspot, opps in zip(reversed(player_info), bench, reversed(matchups)):
#     print(player.text, benchspot.text, opps.text)
#     if opps.text != "--":
#         bench_players_with_games.append(player.text)

# print(bench_players_with_games)
