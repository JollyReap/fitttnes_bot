from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

account = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='☠Удалить аккаунт☠')
        ],
        [
            KeyboardButton(text="🙌А не-не-не, тупанул, оставляй🙌")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True

)
