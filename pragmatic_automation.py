from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def getDriver():
    opts = Options()
    opts.headless = True
    opts.add_argument('--ignore-certificate-errors')
    opts.add_argument('--ignore-ssl-errors')
    opts.add_argument("--log-level=3")
    return Chrome(options=opts)

def getButtonsByText(driver, text):
    driver.get('https://pragmatik.lcsinternalservices.lcs.dev/#/teamstatusreview')
    driver.implicitly_wait(5)
    return driver.find_elements_by_xpath("//*[contains(text(), '{}')]".format(text))

def log_in(driver, username, password):
    driver.get('https://pragmatik.lcsinternalservices.lcs.dev/Account/Login')
    username_field = driver.find_element_by_name("Username")
    password_field = driver.find_element_by_name("Password")
    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

def send_reminder_emails(driver):
    buttons = getButtonsByText(driver, "Notify User")
    for button in buttons:
        button.click()

def send_status_email(driver):
    buttons = getButtonsByText(driver, "Email Daily Statuses")
    buttons[0].click()
    driver.implicitly_wait(5)

def set_dnr(driver):
    buttons = getButtonsByText(driver, "Set Status to DNR")
    for button in buttons:
        button.click()
    driver.implicitly_wait(5)

def send_reminder_task(config):
    driver = getDriver()
    log_in(driver, config['username'], config['password'])
    send_reminder_emails(driver)
    log("[{}] Sending Reminder Emails".format(time.ctime(time.time())))

def send_status_task(config):
    driver = getDriver()
    log_in(driver, config['username'], config['password'])
    set_dnr(driver)
    send_status_email(driver)
    log("[{}] Sending Status Email".format(time.ctime(time.time())))

def log(text):
    with open("output.log", "a") as file:
        file.write("{}\n".format(text))
        print(text)
