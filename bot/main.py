# Стартовый скрипт Telegram-бота (будет использовать aiogram)
# bot/main.py

from data.db import init_db, add_expense
from core.finance import parse_expense_message, categorize_expense
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
init_db()  # запускаем инициализацию БД 
executor.start_polling(dp, skip_updates=True)


@dp.message_handler(lambda msg: msg.text and not msg.text.startswith("/"))
async def handle_expense(message: types.Message):
    category_raw, amount = parse_expense_message(message.text)
    if not category_raw or not amount:
        await message.answer(
            "❌ Неправильный формат. Напиши что-то вроде:\n\n`обед 450`\n`такси 300`\n\n(категория + сумма)",
            parse_mode="Markdown"
        )
        return

    category = categorize_expense(category_raw)
    add_expense(message.from_user.id, category, amount, category_raw)
    await message.answer(f"✅ Записал: *{category}* — `{amount}`₽", parse_mode="Markdown")
