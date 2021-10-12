from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Пройти регистрацию🌐')
        ],
        [
            KeyboardButton(text='Информация о боте📖')
        ],
        [
            KeyboardButton(text='Расчитать ИМТ♎')
        ]
    ],
    resize_keyboard=True
)