from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from loader import dp, db
from keyboards.default.weight import one_or_more
from keyboards.inline.callback_dataes import weight_callback
from keyboards.default.snack_options import snack
from states.food_diary_states import Food_Diary


@dp.message_handler(text='Внести данные✍')
async def choose_snack(message: types.Message, state: FSMContext):
    await message.answer('Какой приём пищи будете вносить?',
                         reply_markup=snack)
    await Food_Diary.next()


@dp.message_handler(state=Food_Diary.choose_value)
async def choose_value(message: types.Message, state: FSMContext):
    await message.answer(f'{message.text}, хорошо!\n'
                         f'Сколько порций у вас (1 или более)',
                         reply_markup=one_or_more)

    await state.update_data(snack=message.text)
    await Food_Diary.next()


@dp.message_handler(text='Одна', state=Food_Diary.product)
async def enter_one_product(message: types.Message, state: FSMContext):
    await message.answer('Введите что вы скушали\n'
                         'Введите точное значение чтобы мы попробывали найти это и записать его параметры')

    await Food_Diary.next()


@dp.message_handler(text='Больше', state=Food_Diary.product)
async def enter_a_lot_products(message: types.Message, state: FSMContext):
    await message.answer('Введите что вы скушали\n'
                         'Введите точное значение чтобы мы попробывали найти это и записать его параметры')

    await Food_Diary.next()


@dp.message_handler(state=Food_Diary.weight)
async def enter_weight(message: types.Message, state: FSMContext):
    await state.update_data(product=message.text)
    await message.answer('Введите ваш вес\n'
                         'Если не хотите просто напишите "нет"')

    await Food_Diary.next()


@dp.message_handler(state=Food_Diary.save_in_db)
async def save_in_db(message: types.Message, state: FSMContext):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    await message.answer(f'Вот что вы ввели:\n'
                         f'{data}')