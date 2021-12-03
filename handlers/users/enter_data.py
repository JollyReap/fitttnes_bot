from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, db
from keyboards.default.reg_from_food_diary import registration
from keyboards.default.snack_options import snack
from states.food_diary_states import Food_Diary


@dp.message_handler(text='Внести данные✍')
async def enter_eating(message: types.Message):
    await message.answer('Какой приём пищи хотите внести?',
                         reply_markup=snack)

    await Food_Diary.next()


@dp.message_handler(state=Food_Diary.product)
async def enter_product(message: types.Message, state: FSMContext):
    await message.answer(f'{message.text}, хорошо!\n'
                         f'Ведите что вы ели')

    eating = await state.update_data(eating=message.text)
    await Food_Diary.next()

