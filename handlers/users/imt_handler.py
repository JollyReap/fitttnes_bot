
from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from states.imt_states import Imt
from keyboards.default.menu import menu


@dp.message_handler('Расчитать ИМТ♎')
async def weight(message: types.Message):
    await message.answer('Введите ваш вес')
    await Imt.height.set()


@dp.message_handler(state=Imt.height)
async def height(message: types.Message, state: FSMContext):
    dirty_weight = message.text
    clear_weight = weight.replace(',', '.')
    await message.answer('Отлично!\n'
                         'Введите ваш рост(в метрах!)')
