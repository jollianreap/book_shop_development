from aiogram import Dispatcher
from aiogram.types import Message, ParseMode


async def admin_start(message: Message):
    await message.reply("Hello, admin!\n"
                        "Вот тебе ссылочка на админ панель(пароль и логин знаешь): <a href='http://127.0.0.1:8000/admin'> Админ Панель</a>", parse_mode=ParseMode.HTML)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
