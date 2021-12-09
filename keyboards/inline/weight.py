from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


weight = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(text='Да👍',
                                                           callback_data='weight:true')
                                  ],
                                  [
                                      InlineKeyboardButton(text='Нет👎',
                                                           callback_data='weight:false')
                                  ]
                              ]
                              )
