import asyncio

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

from app import config


# instances
loop = asyncio.get_event_loop()
bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML, loop=loop)
dispatcher = Dispatcher(bot=bot, storage=MemoryStorage(), loop=loop)


async def on_startup(_):
    """ Executed before the bot starts. """

    ...


async def on_shutdown(_):
    """ Executed after the bot is turned off. """

    ...


# run
if __name__ == '__main__':
    executor.start_polling(dispatcher, loop=loop, on_startup=on_startup,
                           on_shutdown=on_shutdown, fast=False)
