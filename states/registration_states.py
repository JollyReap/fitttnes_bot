from aiogram.dispatcher.filters.state import State, StatesGroup


class Regisistration(StatesGroup):
    nickname_registration = State()
    finaly_registration = State()
