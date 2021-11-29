from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date

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
        driver.implicitly_wait(.5)
    return len(buttons)

def send_status_email(driver):
    buttons = getButtonsByText(driver, "Email Daily Statuses")
    buttons[0].click()
    driver.implicitly_wait(5)

def set_dnr(driver, count=0):
    try:
        buttons = getButtonsByText(driver, "Set Status to DNR")
        for button in buttons:
            button.click()
            driver.implicitly_wait(.5)
        return count if count != 0 else len(buttons)
    except Exception as err:
        log("ERROR: {} ocurred. {}".format(type(err).__name__, err.__str__().strip()))
        set_dnr(driver, count if count != 0 else len(buttons))

def send_reminder_task(config):
    try:
        if str(date.today()) in config["holidays"]:
            log("Canceled by holiday: Reminder Emails")
            return
        driver = getDriver()
        log_in(driver, config['username'], config['password'])
        notification_count = send_reminder_emails(driver)
        log("Sending Reminder Emails: {} sent".format(notification_count))
        time.sleep(30)
        driver.quit()
    except Exception as err:
        log("ERROR: {} ocurred. {}".format(type(err).__name__, err.__str__().strip()))

def send_status_task(config):
    try:
        if str(date.today()) in config["holidays"]:
            log("Canceled by holiday: Status Email")
            return
        driver = getDriver()
        log_in(driver, config['username'], config['password'])
        dnr_count = set_dnr(driver)
        send_status_email(driver)
        log("Sending Status Email: {} DNR".format(dnr_count))
        time.sleep(30)
        driver.quit()
    except Exception as err:
        log("ERROR: {} ocurred. {}".format(type(err).__name__, err.__str__().strip()))
    
def log(text):
    output = "[{}] {}".format(time.ctime(time.time()), text)
    with open("output.log", "a") as file:
        file.write("{}\n".format(output))
        print(output)

def log_heartbeat(text):
    output = "[{}] {}".format(time.ctime(time.time()), text)
    with open("heartbeat.log", "a") as file:
        file.write("{}\n".format(output))
