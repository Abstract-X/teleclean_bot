from aiogram import Bot
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from app.executors import execute_hello, execute_request_chat


async def handle_start_command(update: Message, bot: Bot, fsm_context: FSMContext):
    """ Processing the first press of the start command. """

    await execute_hello(update, bot)
    await execute_request_chat(update, bot, fsm_context)
