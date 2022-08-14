from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests

menu_cd = CallbackData("show_menu", "level", "product_id")

URL = "http://127.0.0.1:8000/api/"


def make_callback_data(level, product_id="-"):
    return menu_cd.new(product_id=product_id, level=level)


async def books_keyboard():
    CURRENT_LEVEL = 0
    markup = InlineKeyboardMarkup()

    all_books = requests.get(f"{URL}all_books/").json()
    for book in all_books:
        number_of_items = book.get('quantity')
        button_text = f'{book.get("product_name")} ({number_of_items}) шт.'

        callback_data = make_callback_data(level=CURRENT_LEVEL, product_id=book.get("id"))
        markup.insert(
            InlineKeyboardButton(text=button_text, callback_data=callback_data)
        )

    return markup


async def book_keyboard(level, product_id):
    CURRENT_LEVEL = 1
    markup = InlineKeyboardButton()

    markup.row(
        InlineKeyboardButton(
            text="Назад",
            callback_data=make_callback_data(level=CURRENT_LEVEL-1,
                                             product_id=product_id))
    )
    return markup


