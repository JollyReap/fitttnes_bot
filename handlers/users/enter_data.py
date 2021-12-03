from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, db
from keyboards.default.reg_from_food_diary import registration
from keyboards.default.snack_options import snack


@dp.message_handler(text='Внести данные✍')
async def enter_data(message: types.Message):
    await message.answer('Какой приём пищи хотите внести?',
                         reply_markup=snack)