from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


weight = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(text='Да👍')
                                  ],
                                  [
                                      InlineKeyboardButton(text='Нет👎')
                                  ]
                              ])