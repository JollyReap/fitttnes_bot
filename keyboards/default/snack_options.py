from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

snack = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='Завтрак')
        ],
        [
            KeyboardButton(text='Полдник')
        ],
        [
            KeyboardButton(text='Обед')
        ],
        [
            KeyboardButton(text='Перекус')
        ],
        [
            KeyboardButton('Ужин')
        ]
    ]
)