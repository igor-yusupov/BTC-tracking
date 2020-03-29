# Bitcoin rate tracking with telegram bot

Using this code, you can create a program that will track the rate of the currency of interest to you and send the current rate to you in a telegram if the price of the currency has changed significantly

## Getting Started

First you need to create a bot and get your chat id in telegram

* [Create Telegram Bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
* [Get Chat Id](https://t.me/ShowJsonBot?info)

Add this data to config.py

## Running on a local machine

The following command will create a new venv directory in your directory in which all local libraries will be stored.

```
virtualenv venv
```

After which we will need to move inside the virtual environment, where it will be possible to load all the necessary packages for the project.

```
source venv/bin/activate
```

After run the script

```
python3 main.py
```
