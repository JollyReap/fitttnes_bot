from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from callback_dataes import weight_callback

weight = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(text='Да👍',
                                                           callback_data=weight_callback.new('weight:true'))
                                  ],
                                  [
                                      InlineKeyboardButton(text='Нет👎',
                                                           callback_data=weight_callback.new('weight:false'))
                                  ]
                              ]
                              )
