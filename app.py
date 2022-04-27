from curses import use_default_colors
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import time
import pandas as pd

#launch url
url = "https://www.barbican.org.uk/whats-on/2022/event/blanca-li-le-bal-de-paris"
# create a new Chrome session
options = Options()
# options.add_argument('--headless')
options.binary_location = r"/usr/bin/google-chrome"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

time.sleep(1)

#get to the "Check sales & book" button
actions = ActionChains(driver)
time.sleep(2)
actions.key_down(Keys.TAB)
actions.key_down(Keys.TAB)
actions.key_down(Keys.TAB)
actions.key_down(Keys.TAB)
actions.key_down(Keys.TAB)
actions.key_down(Keys.TAB)
actions.key_down(Keys.TAB)
actions.key_down(Keys.TAB)
actions.key_down(Keys.TAB)
actions.key_down(Keys.TAB)
actions.key_down(Keys.TAB)
actions.key_down(Keys.TAB)
actions.key_down(Keys.TAB)
actions.key_down(Keys.TAB)
actions.key_down(Keys.TAB)
actions.key_down(Keys.TAB)
actions.key_down(Keys.TAB)
actions.key_down(Keys.TAB)
time.sleep(2)
actions.key_down(Keys.ENTER).perform()
time.sleep(2)
actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
time.sleep(10)
actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

#put status into a big old google sheet (have set it up to check the sold out cells do not change, but if they do...)
gsheets='https://docs.google.com/spreadsheets/d/1vJimhATqKRmUqVMfZuZncP65l67Qd6BLXQYQskZOMCE/edit?usp=sharing' # Used for easy formating
driver.get(gsheets)

actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

time.sleep(5)

# find the cell
actions.key_down(Keys.ARROW_RIGHT).perform()
actions.key_down(Keys.ARROW_RIGHT).perform()
actions.key_down(Keys.ARROW_RIGHT).perform()
actions.key_down(Keys.ARROW_RIGHT).perform()
actions.key_down(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).perform()

#can use a google app / bot from here to get emails around that cell value!
time.sleep(3)


print('done')
