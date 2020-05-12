import asyncio

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

from app import config, middlewares, handlers
from app.services import Cleaner


# instances
loop = asyncio.get_event_loop()
bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML, loop=loop)
dispatcher = Dispatcher(bot=bot, storage=MemoryStorage(), loop=loop)
cleaner = Cleaner(config.TELEGRAM_APP_SESSION_NAME, config.TELEGRAM_APP_ID,
                  config.TELEGRAM_APP_HASH, loop)


async def on_startup(_):
    """ Executed before the bot starts. """

    await cleaner.connect()
    user_id = await cleaner.load_user_id()

    middlewares.setup(dispatcher, bot, cleaner)
    handlers.register_all(dispatcher, user_id, cleaner)


async def on_shutdown(_):
    """ Executed after the bot is turned off. """

    await cleaner.disconnect()


# run
if __name__ == '__main__':
    executor.start_polling(dispatcher, loop=loop, on_startup=on_startup,
                           on_shutdown=on_shutdown, fast=False)
