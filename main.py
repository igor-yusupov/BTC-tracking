import requests
import time
from bs4 import BeautifulSoup
import asyncio
import logging
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN, admin_id
from aiogram.contrib.fsm_storage.memory import MemoryStorage
logging.basicConfig(level=logging.DEBUG)

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage, loop=loop)


class Currency:
    def __init__(self):
        self.differece = 500
        self.BTC_DOLLAR = 'https://www.google.com/search?q=btc+in+dollars&oq=btc+in+dolla&aqs=chrome.1.69i57j0l7.11710j1j4&sourceid=chrome&ie=UTF-8'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        self.current_currency = float(self.get_currency().replace('.', '').replace(',', '.'))

    def get_currency(self):
        page = requests.get(self.BTC_DOLLAR, headers=self.headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde",
                                        "class": "SwHCTb",
                                        "data-precision": 2})
        return convert[0].text

    def check_currency(self):
        currency = self.get_currency()
        currency = currency.replace('.', '')
        return float(currency.replace(',', '.'))


async def send_to_admin(*args):
    while True:
        time.sleep(60)
        currency = Currency()
        btc = currency.check_currency()
        current = currency.current_currency
        if abs(current - btc) > currency.differece:
            await bot.send_message(chat_id=admin_id, text="Now Bitcoin costs {}$".format(str(btc)))
            currency.current_currency = btc
        else:
            pass


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=send_to_admin)
