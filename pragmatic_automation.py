from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def getDriver():
    opts = Options()
    opts.headless = True
    opts.add_argument('--ignore-certificate-errors')
    opts.add_argument('--ignore-ssl-errors')
    return Chrome(options=opts)

def log_in(driver, username, password):
    driver.get('https://pragmatik.lcsinternalservices.lcs.dev/Account/Login')
    print(driver.title)
    username_field = driver.find_element_by_name("Username")
    password_field = driver.find_element_by_name("Password")
    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    print(driver.current_url)

def send_reminder_emails(driver):
    print("Not implemented: sending emails")

def send_status_email(driver):
    print("Not implemented: sending emails")

def set_dnr(driver):
    print("Not implemented: set dnr")

def sendReminders(config):
    driver = getDriver()
    log_in(driver, config['username'], config['password'])

def sendEmail(config):
    driver = getDriver()
    log_in(driver, config['username'], config['password'])
    set_dnr(driver)
    send_status_email(driver)
