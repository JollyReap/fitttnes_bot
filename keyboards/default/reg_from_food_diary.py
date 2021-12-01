from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

registration = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Пройти сейчас')
        ],
        [
            KeyboardButton(text='Позже сам(а) пройду')
        ]
    ]
)