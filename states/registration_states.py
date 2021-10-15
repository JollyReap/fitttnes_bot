from aiogram.dispatcher.filters.state import State, StatesGroup


class Regisistration(StatesGroup):
    email_registration = State()
    password_registration = State()
    nickname_registration = State()
