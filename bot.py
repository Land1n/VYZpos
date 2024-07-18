import asyncio
import os

from aiogram import Bot,Dispatcher
from aiogram.types import Message
from aiogram.filters import Command,CommandStart

from api import get_position_in_university

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Напиши команду: /position - чтобы узнать на каком я месте')

@dp.message(Command('position'))
async def cmd_get_position(message: Message):
    position, info = get_position_in_university()
    await message.answer(f"Иван на {position} месте.\n\nМест на бюджет: {info['total_num']}.\n\nНаправление: {info['name']}")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    print('Бот включен')
    try:
        asyncio.run(main()) 
    except KeyboardInterrupt:
        print('Бот выключен')