from aiogram import Dispatcher
from aiogram.types import Message
from ..keyboards.reply import main_keyboard
import requests


async def user_start(message: Message):
    await message.reply(f"Привет, {message.from_user.username}!\n"
                        f"Щас проверю есть ли ты в базе")
    response = requests.get(f'http://127.0.0.1:8000/apiv2/check_user/{message.from_user.id}')
    if response.status_code == 200:
        await message.reply("Отлично, ты есть в базе", reply_markup=main_keyboard)
    elif response.status_code == 500:
        await message.reply("Тебя нету в базе, но это не проблема, щас создам тебе аккаунт, секундочку...")
        create = requests.post("http://127.0.0.1:8000/apiv2/create_user/", data={"telegram_id": message.from_user.id,
                                                                                 "username": message.from_user.username})
        if create.status_code == 200 or create.status_code == 201:
            await message.reply("Добро пожаловать в семью "
                                , reply_markup=main_keyboard)

        else:
            await message.reply(f"Проблемка тут, попробуй ещё раз")

def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
