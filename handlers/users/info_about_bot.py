from aiogram import types

from loader import dp


@dp.message_handler(text="Информация о боте📖")
async def info(message: types.Message):
    await message.answer('Данный бот - проектная работа')
