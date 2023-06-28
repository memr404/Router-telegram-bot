import asyncio, logging
import connect 

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.webhook import RestrictChatMember
from aiogram.types import ChatActions
from aiogram.utils.markdown import hlink


token = '5834123801:AAG1ZyMbaWdafaLle2vryX29P1J0L1iTLyk'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)


@dp.message_handler()
async def start(message: types.Message,state: FSMContext):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup.row(types.KeyboardButton(f'🔄Перезагрузить роутер'))
	markup.row(types.KeyboardButton(f'👥Показать клиентов'))
	if message.text == '/start':
		await bot.send_message(message.chat.id, '❓Что нужно сделать?', reply_markup=markup)
	
	elif message.text == '🔄Перезагрузить роутер':
		connect.off()
		await bot.send_message(message.chat.id, '🔄Бот начал перезагружаться! ⏱Ожидайте!', reply_markup=markup)

	elif message.text == '👥Показать клиентов':
		await bot.send_message(message.chat.id, connect.get(), reply_markup=markup)

######
async def main():
	await dp.start_polling(bot)


if __name__ == '__main__':
	asyncio.run(main())