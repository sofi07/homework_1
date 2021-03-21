from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from homework_1.keyboards_1 import *

# from config import TOKEN
from state import States

TOKEN = '1620272486:AAFVmhtB5fFDo9mgKA8A83_kpVoKTnq96hQ'

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(CommandStart())
async def hello(message: types.Message, state: FSMContext):
    await message.answer(text='Здравствуйте. Как я могу к вам обращаться?')
    await States.Name.set()


@dp.message_handler(state=States.Name)
async def name(message: types.Message, state: FSMContext):
    await message.answer(text=f'{message.text} , очень приятно. Уточните, откуда нужно забрать документы?')
    await States.From.set()


@dp.message_handler(state=States.From)
async def from_1(message: types.Message, state: FSMContext):
    await message.answer(
        text='Ближайшее время,в которое сможем забрать - <БЛИЖАЙШЕЕ ВРЕМЯ>. Вам будет удобно, или вы хотите позже?',
        reply_markup=from_time)
    await States.From_Time.set()


@dp.message_handler(lambda x:
                    x.text == 'Ближайшее',
                    state=States.From_Time)
async def address(message: types.Message, state: FSMContext):
    await message.answer(text='Теперь уточните адрес, по которому документы нужно отвезти.',
                         reply_markup=ReplyKeyboardMarkup(
                             [
                                 [KeyboardButton(text='Подходит'),
                                  KeyboardButton(text='Срочная')],
                                 [KeyboardButton(text='Ко времени')]
                             ],
                             resize_keyboard=True))
    await States.Address.set()




if __name__ == '__main__':
    executor.start_polling(dp)
