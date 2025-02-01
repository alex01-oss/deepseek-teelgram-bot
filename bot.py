import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from aiogram import types
from aiogram.types import Message
from aiogram.filters import Command
import requests

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7810092883:AAHhtQFxgRnfc41oOX0wMCREHRGNOQcZLXE")  # your token
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    start_text = "Welcome to @direcode"
    await bot.send_message(message.chat.id, start_text)


@dp.message()
async def message_handler(msg: Message):
    stream = False
    url = "https://proxy.tune.app/chat/completions"
    headers = {
        "Authorization": "sk-tune-S1umHH1xGSyuVwZ4VR8DRe78QtBt41Dzv2o",
        "Content-Type": "application/json",
    }

    data = {
        "temperature": 0.8,
        "messages": [
            {"role": "user", "content": msg.text},
        ],
        "model": "deepseek/deepseek-r1",
        "stream": stream,
        "frequency_penalty": 0,
        "max_tokens": 900,
    }

    response = requests.post(url, headers=headers, json=data)
    data = response.json()
    text = data["choices"][0]["message"]["content"]

    await bot.send_message(msg.chat.id, text, parse_mode="Markdown")


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
