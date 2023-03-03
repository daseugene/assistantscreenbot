from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor 
import kb


from utils import MainStates



bot = Bot(token='6039398231:AAG_0GULdnOPYoeUdo3TCY5m1fl2LOCZV-U')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'], state=None)
async def command_start(message: types.Message):
    await message.answer("Привет. Введи пароль: ")
    await MainStates.awaiting_password.set()
    


@dp.message_handler(state=MainStates.awaiting_password)
async def check_password(message: types.Message):
    if message.chat.id == '1' or '2':
        await message.answer("Доступ есть")
    await MainStates.ready_to_work.set()



@dp.callback_query_handler(state=MainStates.ready_to_work, text='send_code')
async def work(query: types.CallbackQuery):
    pass
    


if __name__ == '__main__':
    print('Starting bot...')
    executor.start_polling(dp, skip_updates=True)



