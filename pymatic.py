from pragmatic_automation import * 
import json
import schedule
import time
import datetime
from os.path import exists
import sys

last_heartbeat = 0
POLL_FQ = 15

def task_heartbeat():
    global last_heartbeat
    last_heartbeat = 0
    log_heartbeat("Task Heartbeat")

try:
    with open('config.json', 'r') as file:
        config = json.loads(file.read())
    if config['username'] == "":
        raise Exception()
except:
    print("ERROR: Please configure config.json before running. See readme for more details.")
    input("Press enter to close")
    sys.exit()

if not exists('chromedriver.exe'):
    print("ERROR: `chromedrive.exe` was not found. Please download a driver matching your version of Chrome from https://chromedriver.chromium.org/downloads and place into the same directory as `pymatic.exe` making sure to rename it `chromedriver.exe`")
    input("Press enter to close")
    sys.exit()

def start_tasks():
    try:
        if 'reminderTimes' in config.keys():
            for time in config['reminderTimes']:
                schedule.every().day.at(time).do(send_reminder_task, config).tag('task')
        else:
            schedule.every().day.at(config["reminderTime"]).do(send_reminder_task, config).tag('task')
        schedule.every().day.at(config["sendTime"]).do(send_status_task, config).tag('task')
        schedule.every(POLL_FQ).seconds.do(task_heartbeat).tag('task')
        log("Starting Pymatic Tasks, leave this terminal running")
    except Exception as err:
        print("ERROR: {} ocurred. {}".format(type(err).__name__, err.__str__().strip()))
        input("Press enter to close")
        sys.exit()

def clear_tasks():
    schedule.clear('task')
    log("Clearing Pymatic Tasks")

def start_system_tasks():
    schedule.clear('system')
    schedule.every().monday.at("00:00").do(start_tasks).tag('system')
    schedule.every().saturday.at("00:00").do(clear_tasks).tag('system')
    log("Starting system tasks")

start_system_tasks()

if datetime.datetime.today().weekday() < 5:
    start_tasks()
else:
    log("Pymatic will start on Monday, leave this terminal running")

while True:
    last_heartbeat += POLL_FQ
    schedule.run_pending()
    if last_heartbeat > POLL_FQ * 2:
        log("Heartbeat timed out, restarting pymatic")
        clear_tasks()
        start_tasks()
        start_system_tasks()
    time.sleep(POLL_FQ)
