from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ..inline.callbackdata_delete import callback_true_false
choice = InlineKeyboardMarkup(
                            row_width=2,
                            inline_keyboard=[
                                [
                                    InlineKeyboardButton(
                                        text='☠Удалить аккаунт☠',
                                        callback_data=callback_true_false.new(status='true')
                                    ),
                                [
                                    InlineKeyboardButton(
                                        text='🙌А не-не-не-не, перепутал🙌',
                                        callback_data=callback_true_false.new(status='false')
                                    )
                                ]
                                ]
                            ]
)