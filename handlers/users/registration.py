import validators
from aiogram import types
from aiogram.dispatcher import FSMContext
from utils.dp_api.models import Users
from keyboards.default.menu import menu
from keyboards.default.stop_autorise import stop
from loader import dp, db
from states.registration_states import Regisistration
from keyboards.default.del_acc import account


@dp.message_handler(text="❌Остановить регистрацию❌", state='*')
async def stop_autorise(call: types.Message, state: FSMContext):
    await call.answer('Регистрация остановлена!',
                      reply_markup=menu)
    await state.finish()


@dp.message_handler(text="Пройти регистрацию🌐")
async def get_email(message: types.Message):
    if db.select_user(message.from_user.id):
        await message.answer('Отлично!')
        await message.answer('Ведите ваш email📧',
                             reply_markup=stop)
        await Regisistration.nickname_registration.set()
    else:
        await message.answer('Вы уже есть в базе!\n'
                             'Вы хотите удалить своего пользователя?',
                             reply_markup=account)


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
    tg_id = str(message.from_user.id)
    dict_id = {'tg_id': tg_id,
               'email': email,
               'nickname': nickname}

    db.add_registration_info(data=dict_id, model=Users, filter_field='tg_id')
    await message.answer('Спасибо за регистрацию!',
                         reply_markup=menu)
    await state.finish()
