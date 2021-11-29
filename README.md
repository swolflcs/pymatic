# Pymatic

Pymatic automates pragmatic with selenium

## Getting started

To get started you will need a few things

1. install python 3
2. run `pip3 install selenium schedule`
4. download chromedriver for your version of chrome and place the exe into the 
   root of your pymatic folder [download directory](https://chromedriver.chromium.org/downloads)
3. in the root directory create and fill out config.js with the following format

```
{
    "username": "your username here",
    "password": "your password here",
    "reminderTime": "HH:MM" OR "reminderTimes": ["HH:MM", ...]
    "sendTime": "HH:MM",
    "holidays": ["YYYY-MM-DD", ...]
}
```

NOTE: Time is in military format (ex: 6pm == 18:00)

## Features

- Sends reminders and the status email at the times specified in the config
- Turns off during the weekend and on holidays specified in the config
- Keeps a log of activity in output.log

## Running Pymatic

1. Open your favorite terminal
2. Type `python3 pymatic.py` to start the daemon
3. CTRL+C to interrupt the script

## Building Pymatic

```
pyinstaller --onefile .\pymatic.py
```