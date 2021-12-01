from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

registration = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
    keyboard=[
        [
                KeyboardButton(text='Пройти сейчас')
            ],
            [
                KeyboardButton(text='Позже сам(а) пройду')
            ]
        ]
)