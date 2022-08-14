from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=[
    [
        KeyboardButton(text="Все книги📚"),
        KeyboardButton(text="Категории🎯"),
        KeyboardButton(text="Искать книгу🔎")

    ]
])


