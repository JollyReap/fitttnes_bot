from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


weight = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(text='ะะฐ๐',
                                                           callback_data='weight:true')
                                  ],
                                  [
                                      InlineKeyboardButton(text='ะะตั๐',
                                                           callback_data='weight:false')
                                  ]
                              ]
                              )
