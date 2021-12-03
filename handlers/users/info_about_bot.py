from aiogram import types
from keyboards.default.menu import menu
from loader import dp


@dp.message_handler(text="Информация о боте📖")
async def info(message: types.Message):
    await message.answer('Данный бот - проектная работа',
                         reply_markup=menu)
