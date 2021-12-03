from aiogram import types
from keyboards.default.menu import menu
from loader import dp, db
from keyboards.default.food_diary_buttons import food_diary
from keyboards.default.reg_button import button


@dp.message_handler(text='Дневник питания📔')
async def check_status(message: types.Message):
    await message.answer('Проверяю есть ли ты в базе...')
    if db.select_user(message.from_user.id):
        await message.answer('Отлично! Ты зарегестрирован(а)\n'
                             'Выбирай что будем делать😀',
                             reply_markup=food_diary)

    else:
        await message.answer('Тебе надо зарегестрироваться чтобы вести дневник!\n'
                             'Хочешь сделать это сейчас?', reply_markup=button)


@dp.message_handler(text='Назад⬅')
async def back(message: types.Message):
    await message.answer(text='...',
                         reply_markup=menu)
