from aiogram.utils.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests

menu_cd = CallbackData("show_menu", "level", "category_id")
main_menu = CallbackData("main_menu", "command")


URL = "http://127.0.0.1:8000/api/"
main_menu_keyboard = InlineKeyboardMarkup()

main_menu_keyboard.insert(InlineKeyboardButton(text="Все книги📚", callback_data=main_menu.new(command="all_books")))
main_menu_keyboard.insert(InlineKeyboardButton(text="Категории🎯", callback_data=main_menu.new(command="categories")))
main_menu_keyboard.insert(InlineKeyboardButton(text="Искать книгу🔎", callback_data=main_menu.new(command="search")))


def make_callback_data(level, category_id=0):
    return menu_cd.new(category_id=category_id, level=level)


async def category_keyboard():
    CURRENT_LEVEL = 0
    CURRENT_CATEGORY = 0
    markup = InlineKeyboardMarkup()

    all_categories = requests.get(f"{URL}all_category/").json()
    for category in all_categories:

        callback_data = make_callback_data(level=CURRENT_LEVEL+1, category_id=category.get("id"))
        markup.insert(
            InlineKeyboardButton(text=str(CURRENT_CATEGORY), callback_data=callback_data)
        )
        CURRENT_CATEGORY += 1

    return markup


async def books_keyboard(level, category_id):
    CURRENT_LEVEL = 1
    CURRENT_BOOK = 0
    markup = InlineKeyboardMarkup()

    books_by_category = requests.get(f'{URL}/filter_category/{category_id}')
    for book in books_by_category:
        callback_data = make_callback_data(level=CURRENT_LEVEL, category_id=category_id)
        markup.insert(
            InlineKeyboardButton(text=str(CURRENT_BOOK), callback_data=callback_data)
        )
