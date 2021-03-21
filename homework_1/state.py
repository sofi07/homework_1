from aiogram.dispatcher.filters.state import State, StatesGroup

class States(StatesGroup):
    Name = State()
    From = State()
    From_Time = State()
    From_Time_later = State()
    Address = State()
