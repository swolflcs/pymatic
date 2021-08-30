# Pymatic

Pymatic automates pragmatic with selenium

## Getting started

To get started you will need a few things

1. install python 3
2. run `pip3 install selenium schedule`
4. download chromedriver for your version of chrome and place the exe into the 
   root of your pymatic folder [download directory](https://chromedriver.chromium.org/downloads)
3. in the root directory create and fill out config.js with the following format

    {
        "username": "your username here",
        "password": "your password here",
        "reminderTime": "HH:MM",
        "sendTime": "HH:MM"
    }

NOTE: Time is in military format (ex: 6pm == 18:00)
