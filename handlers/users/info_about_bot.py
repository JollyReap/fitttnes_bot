from aiogram import types

from loader import dp


@dp.message_handler(text="Информация о боте📖")
async def info(message: types.Message):
    await message.answer('Данный бот - проектная работа\n'
                'Исходный код будет выложен на <a href="https://github.com/v1ntec">GitHub</a>', parse_mode=types.ParseMode.HTML)