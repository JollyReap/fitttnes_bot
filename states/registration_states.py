from aiogram.dispatcher.filters.state import State, StatesGroup


class Regisistration(StatesGroup):
    password_registration = State()
    nickname_registration = State()
    finaly_registration = State()
