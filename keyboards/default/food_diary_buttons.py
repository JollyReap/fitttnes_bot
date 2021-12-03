from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

food_diary = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='Внести данные✍')
        ],
        [
            KeyboardButton(text='Посмотреть график худения🏋')
        ],
        [
            KeyboardButton(text='Назад⬅')
        ]
    ]
    )

# It isn`t finish version buttons