from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ..inline.callback_data_torf import callback_true_false

true_or_false = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        InlineKeyboardButton(
                    text='❌Остановить регистрацию❌',
                    callback_data=callback_true_false.new(status='false')
        )
    ]
)