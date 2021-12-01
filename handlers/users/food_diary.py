from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp, db
from keyboards.default.reg_from_food_diary import registration
from keyboards.default.reg_button import button


@dp.message_handler(text='Дневник питания📔')
async def check_status(message: types.Message):
    await message.answer('Проверяю есть ли ты в базе...')
    if db.select_user(message.from_user.id):
        await message.answer('Отлично! Ты зарегестрирован(а)\n'
                             'Выбирай что будем делать😀')

    else:
        await message.answer('Тебе надо зарегестрироваться чтобы вести дневник!\n'
                             'Хочешь сделать это сейчас?', reply_markup=button)
