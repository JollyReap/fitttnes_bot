from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Пройти регистрацию🌐')
        ],
        [
            KeyboardButton(text='Информация о боте📖')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)