from pragmatic_automation import * 
import json
import schedule
import time

with open('config.json', 'r') as file:
    config = json.loads(file.read())

def start_tasks():
    schedule.every().day.at(config["reminderTime"]).do(send_reminder_emails, config).tag('workday')
    schedule.every().day.at(config["sendTime"]).do(send_status_email, config).tag('workday')

def kill_tasks():
    schedule.clear('workday')

schedule.every().monday.at("00:00").do(start_tasks)
schedule.every().saturday.at("00:00").do(kill_tasks)
start_tasks()

driver = getDriver()
log_in(driver, config['username'], config['password'])

driver.get('https://pragmatik.lcsinternalservices.lcs.dev/#/teamstatusreview')
driver.implicitly_wait(1)
attribute_value = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3"))).get_attribute("innerHTML")
print(attribute_value)

while True:
    schedule.run_pending()
    time.sleep(1)