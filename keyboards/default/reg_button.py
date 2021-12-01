from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
    keyboard=[
       [
           KeyboardButton(text='Пройти регистрацию🌐')
       ]
    ]
)