import validators
from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.menu import menu
from keyboards.default.stop_autorise import stop
from loader import dp
from states.registration_states import Regisistration


@dp.message_handler(text="❌Остановить регистрацию❌", state='*')
async def stop_autorise(call: types.Message, state: FSMContext):
    await call.answer('Регистрация остановлена!',
                      reply_markup=menu)
    await state.finish()


@dp.message_handler(text="Пройти регистрацию🌐")
async def get_email(message: types.Message):
    await message.answer('Отлично!')
    await message.answer('Ведите ваш email📧',
                         reply_markup=stop)
    await Regisistration.nickname_registration.set()


@dp.message_handler(state=Regisistration.nickname_registration)
async def create_nickname(message: types.Message, state: FSMContext):
    valid_email = validators.email(message.text)
    if valid_email is True:
        await message.answer('Добавляю в базу...\n'
                             'Теперь придумайте имя пользователя!',
                             reply_markup=stop)
        await state.update_data(email=message.text)
        await Regisistration.finaly_registration.set()
    else:
        await message.answer('Ваш email ведён не верно!\n'
                             'Повторите попытку ещё раз',
                             reply_markup=stop)
        if valid_email is True:
            await state.update_data(email=message.text)
            await Regisistration.nickname_registration.set()


@dp.message_handler(state=Regisistration.finaly_registration)
async def finaly(message: types.Message, state: FSMContext):
    data = await state.get_data()
    email = data.get('email')
    password = data.get('password')
    nickname = message.text
    await message.answer('Вот ваши данные, советуем занести их в избранные!\n'
                         f'Ваш email: {email}\n'
                         f'Ваше имя пользователя: {nickname}')
    await state.finish()