from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage



storage = MemoryStorage

class MainStates(StatesGroup):
    awaiting_password = State()
    ready_to_work = State()

