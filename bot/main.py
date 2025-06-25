# Стартовый скрипт Telegram-бота (будет использовать aiogram)
# bot/main.py

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот для учёта трат и настроения. Готов к работе!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
