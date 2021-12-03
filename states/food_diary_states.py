from aiogram.dispatcher.filters.state import State, StatesGroup


class Food_Diary(StatesGroup):
    product = State()
    weight = State()
    save_in_db = State()

# Can change