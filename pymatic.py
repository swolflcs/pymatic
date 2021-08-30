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

print("Pymatic has started, leave this terminal running")
while True:
    schedule.run_pending()
    time.sleep(15)