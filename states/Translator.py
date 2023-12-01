from aiogram.dispatcher.filters.state import State, StatesGroup

class Holat(StatesGroup):
    input = State()
    output = State()
    text = State()
