from pragmatic_automation import * 
import json
import schedule
import time
import datetime

with open('config.json', 'r') as file:
    config = json.loads(file.read())

def start_tasks():
    schedule.every().day.at(config["reminderTime"]).do(send_reminder_task, config).tag('workday')
    schedule.every().day.at(config["sendTime"]).do(send_status_task, config).tag('workday')

def kill_tasks():
    schedule.clear('workday')

schedule.every().monday.at("00:00").do(start_tasks)
schedule.every().saturday.at("00:00").do(kill_tasks)

if datetime.datetime.today().weekday() < 5:
    start_tasks()
    log("Pymatic has started, leave this terminal running")
else:
    log("Pymatic will start on Monday, leave this terminal running")

while True:
    schedule.run_pending()
    time.sleep(15)