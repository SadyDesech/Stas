import asyncio
import logging
import random
from aiogram import Bot,Dispatcher,types
from aiogram.filters import Command,CommandStart
from aiogram.methods import SendPhoto
import requests

import config

dp = Dispatcher()

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    button=[
        [
            types.KeyboardButton(text='/cats')
        ],
    ]
    keaboard=types.ReplyKeyboardMarkup(
        keyboard=button,
        resize_keyboard=True,
        input_field_placeholder="Choose type of photo"
    )
    await message.answer(text=f"Hello, {message.from_user.full_name}! I'm send some cat pics! Choose what u want:",reply_markup=keaboard)

@dp.message(Command('help'))
async def handle_help(message: types.Message):
    text = "I'm send some pics!"
    await message.answer(text=text)
    text = "write /cats to get cat pics"
    await message.answer(text=text)

@dp.message(Command("cats"))
async def cat_photo(message:types.ChatPhoto):
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    await message.bot.send_photo(photo=response.json()[0]["url"],chat_id=message.chat.id)

@dp.message()
async def Massage_answer(message: types.Message):
    answer=["What?","I'm don't understand you!","Send me /cats!","...","Something new))","Okey??","se normal commands!!"]
    await message.answer(
        text=random.choice(answer)
    )


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())