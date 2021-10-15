from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

stop = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('❌Остановить регистрацию❌')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
