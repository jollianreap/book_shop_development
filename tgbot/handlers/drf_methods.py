from typing import Union

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery
from ..keyboards.reply import main_keyboard
from ..keyboards.inline import books_keyboard, menu_cd, book_keyboard
import requests
# Dispatcher.message_handler()
URL = "http://127.0.0.1:8000/api/"


async def get_all_books(message: Message):

    await list_books(message)

    # await message.reply(all_books)


async def list_books(message: Union[CallbackQuery, Message], **kwargs):
    markup = await books_keyboard()

    await message.reply(f"Вот что у нас есть\n\n\n", reply_markup=markup)


async def certain_book(callback: CallbackQuery, product_id, **kwargs):
    markup = await book_keyboard(product_id=product_id, **kwargs)

    book = requests.get(f'{URL}/filter_product/{product_id}').json()

    text = f"""
        Название: {book.get('name')} \n
        Описание: {book.get('description')} \n
        Кол-во на складе: {book.get('quantity')} \n
        Цена: {book.get('price')}
    """

    await callback.message.edit_text(text=text, reply_markup=markup)


async def navigate(call: CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    product_id = callback_data.get('product_id')

    levels = {
        "0": list_books,
        "1": certain_book

    }

    current_level_function = levels[current_level]

    await current_level_function(
        call,
        product_id=product_id
    )


def register_all_books(dp: Dispatcher):
    dp.register_message_handler(get_all_books, state='*', text="Все книги📚")
    dp.register_callback_query_handler(menu_cd.filter())



#
# План работы :
# 1. Добавить возможность перехода из категории
# 2. Нажимая на книгу, показывать все её параметры в бд
# 3. Добавить в Product: author, накатить миграции
# 4. Начать делать поиск по названию и автору