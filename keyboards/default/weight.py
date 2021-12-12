from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

one_or_more  = ReplyKeyboardMarkup(row_width=2,
                                   resize_keyboard=True,
                                   keyboard=[
                                       [
                                           KeyboardButton(text='Одна')
                                       ],
                                       [
                                           KeyboardButton(text='Больше')
                                       ]
                                   ])