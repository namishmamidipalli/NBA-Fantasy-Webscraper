# from flask import Flask, render_template, jsonify
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
from datetime import date
import calendar

# today = date.today()
# print("Today's date:", today.day)
# year = today.year
# month = today.month
# day  = today.day

# lastday = calendar.monthrange(2024, 2)
# lastday = lastday[1]


# app = Flask(__name__)

# @app.route('/')
# def index():
#     # Your scraping logic here
#     driver = webdriver.Chrome()  # Use the appropriate WebDriver
#     driver.get('https://www.espn.com/')
#     time.sleep(8)

    # search_box = driver.find_element(by=By.ID, value='global-user-trigger')
    # search_box.click()
    # time.sleep(2)
    # print('Open Log In Tab')
    # # Click on the Log In location
    # nextbox = driver.find_element(by=By.XPATH, value="//a[@data-affiliatename='espn']")
    # print(nextbox.text)
    # nextbox.click()
    # print('Click Login')
    # #Switch to iFrame to enter log in credentials
    # driver.implicitly_wait(7.0)
    # time.sleep(3.0)


    # driver.switch_to.frame("oneid-iframe")

    # actual_link = driver.find_element(by=By.LINK_TEXT, value="Looking for username login?")
    # print(actual_link.text)
    # actual_link.click()

    # username = driver.find_element(by=By.ID, value="InputLoginValue")


    # time.sleep(2)
    # username.send_keys('namishkmami@gmail.com')
    # # password = driver.find_element_by_xpath("//input[@placeholder='Password (case sensitive)']")
    # password = driver.find_element(by=By.ID, value="InputPassword")
    # password.send_keys('Abhish09')
    # time.sleep(2)
    # # print('Logging In')
    # # # ##Submit credentials
    # submit_button = driver.find_element(by=By.ID, value="BtnSubmit")
    # submit_button.click()
    # time.sleep(10.0)

    # driver.switch_to.default_content()


    # search_box = driver.find_element(by=By.ID, value='global-user-trigger')
    # search_box.click()
    # ##Selecting Fantasy League
    # time.sleep(2)
    # leaguego = driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Namish')
    # leaguego.click()

    # driver.implicitly_wait(4.0)
    # time.sleep(4.0)
    # print('Going to Fantasy Link')



    # time.sleep(4.0)
    # driver.switch_to.default_content()

#     calendar = driver.find_element(by=By.XPATH, value="//button[@aria-label='Calendar' and @class='DateCarousel__MonthTrigger']")
#     calendar.click()
#     driver.implicitly_wait(4.0)


    
#     date = driver.find_element(by=By.XPATH, value="//li[@class='MonthContainer__Day MonthContainer__Day--noEvent' and text()='21']")
#     date.click()
#     # calendar.click()

#     time.sleep(4.0)
#     page = driver.page_source
#     soup = BeautifulSoup(page, 'html.parser')


#     # bench = soup.findAll('td', {'class': 'Table__TD Table__TD--fixed-width', 'style': 'width: 60px;'})
#     pos = soup.findAll('div', attrs={'class': 'jsx-2810852873 table--cell'})
#     player_info = soup.findAll('div', attrs={"class": "jsx-1811044066 player-column__bio"})
#     matchups = soup.findAll('div', attrs={"class": "jsx-2810852873 table--cell opp ml4"})

#     # players = soup.findAll('td', {'class': 'Table__TD Table__TD--fixed-width', 'style': 'width: 228px;'})
#     # borderplayer = soup.findAll('td', {'class': 'Table__TR Table__TR--lg Table__odd Table__border-row'})
#     players = soup.findAll('div', attrs={'class': 'jsx-1811044066 player-column__athlete flex'})

#     playing_but_bench = []

    # target_elements = soup.find_all('tr', class_=['Table__TR Table__TR--lg Table__odd', 'Table__TR Table__TR--lg Table__odd Table__border-row'])
    # for element in target_elements:
    #     if "Bench" in element.text and "--" not in element.text:
    #         playing_but_bench.append(element.text)


#     return render_template('index.html', playing_but_bench=playing_but_bench)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# from datetime import date, calendar

app = Flask(__name__)

def get_bench_players(soup, driver, day):

    playing_but_bench = []
    target_elements = soup.find_all('tr', class_=['Table__TR Table__TR--lg Table__odd', 'Table__TR Table__TR--lg Table__odd Table__border-row'])
    for element in target_elements:
        if "Bench" in element.text and "--" not in element.text:
            playing_but_bench.append(element.text)


    return playing_but_bench

@app.route('/')
def index():
    today = date.today()
    year = today.year
    month = today.month
    lastday = calendar.monthrange(year, month)[1]

    driver = webdriver.Chrome()  # Use the appropriate WebDriver
    driver.get('https://www.espn.com/')
    time.sleep(8)

   
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


    # Navigate to the calendar
    calendar_button = driver.find_element(by=By.XPATH, value="//button[@aria-label='Calendar' and @class='DateCarousel__MonthTrigger']")
    calendar_button.click()
    time.sleep(4.0)

    all_bench_players = []

    # Loop through every day from the current day to the end of the month
    for day in range(today.day + 1, lastday + 1):
        # Locate and click on the specific day in the calendar
        day_element = driver.find_element(by=By.XPATH, value=f"//li[@class='MonthContainer__Day MonthContainer__Day--noEvent' and text()='{day}']")
        day_element.click()

        time.sleep(4.0)
        page = driver.page_source
        soup = BeautifulSoup(page, 'html.parser')

        # Extract bench players for the current day
        playing_but_bench = get_bench_players(soup, driver, day)

        # Append the results to the list
        all_bench_players.append({
            'day': day,
            'bench_players': playing_but_bench
        })

    # Close the driver after all iterations
    driver.quit()

    return render_template('index.html', all_bench_players=all_bench_players)

if __name__ == '__main__':
    app.run(debug=True)
