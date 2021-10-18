# Pymatic

Pymatic automates pragmatic with selenium

## Getting started

To get started you will need a few things

1. download chromedriver for your version of chrome and place the exe into the 
   root of your pymatic folder [download directory](https://chromedriver.chromium.org/downloads)
2. in the root directory create and fill out config.js (see format below)
3. run `pymatic.exe`

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

## Troubleshooting

- If you are get an error in your which prevents a task from running verify
  that your version of chrome matches your version of chromedriver
- If nothing is happening verify that the password and username in your config
  are correct
