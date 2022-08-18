from typing import Union

from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from ..keyboards.inline import category_keyboard, books_keyboard ,menu_cd
import requests
# Dispatcher.message_handler()
URL = "http://127.0.0.1:8000/api/"


async def get_all_categories(message: CallbackQuery):

    await list_categories(message)

    # await message.reply(all_books)


async def list_categories(message: CallbackQuery, **kwargs):
    markup = await category_keyboard()
    categories = [category.get('name') for category in requests.get(f'{URL}all_category/').json()]

    indexed_list = {}

    new_list = [indexed_list.__setitem__(item, i) for i, item in enumerate(categories, start=0)]
    text = "Категории: \n"
    for k, v in indexed_list.items():
        text += f'{v} {k}\n'

    await message.message.reply(text, reply_markup=markup)


# async def list_books(message: CallbackQuery, category_id, **kwargs):
#     markup = await books_keyboard(category_id=category_id)
#     books = [book.get('author_name',
#                       'product_name') for book in requests.get(f'{URL}/filter_category/{category_id}').json()]
#     print(books)
#

async def navigate(call: CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')
    category_id = callback_data.get('category_id')

    levels = {
        "0": list_categories,
        # "1": list_books

    }

    current_level_function = levels[current_level]

    await current_level_function(
        call,
        category_id=category_id
    )


def register_all_books(dp: Dispatcher):
    dp.register_callback_query_handler(get_all_categories, state='*', text_contains="all_books")
    dp.register_callback_query_handler(menu_cd.filter())