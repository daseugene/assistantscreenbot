from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor 

from utils import MainStates
from services import MainService
from authorization import authorize


bot = Bot(token='6039398231:AAG_0GULdnOPYoeUdo3TCY5m1fl2LOCZV-U')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'], state=None)
async def command_start(message: types.Message):
    await message.answer("Привет. Введи пароль: ")
    await MainStates.awaiting_password.set()


@dp.message_handler(state=MainStates.awaiting_password)
async def check_password(message: types.Message):
    success = await MainService.password_check(message.text)

    if success:
        await message.answer("Теперь ты можешь пользоваться ботом, " + message.from_user.full_name)
        await MainStates.ready_to_work.set()
    else:
        await message.answer("Пароль неверный, иди в жопу")
        await MainStates.awaiting_password.set()
        await check_password()



if __name__ == '__main__':
    print('Starting bot...')
    executor.start_polling(dp, skip_updates=True)

