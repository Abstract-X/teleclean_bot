from aiogram import Bot
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from app.executors import execute_chat_cleaning, execute_request_chat, execute_incorrect_chat
from app.services import Cleaner


async def handle_chat_message(update: Message, bot: Bot, cleaner: Cleaner):
    """ Processing sent chat data. """

    await execute_chat_cleaning(update, bot, cleaner)


async def handle_incorrect_chat_message(update: Message, bot: Bot):
    """ Processing sent incorrect chat data. """

    await execute_incorrect_chat(update, bot)


async def handle_start_command(update: Message, bot: Bot, fsm_context: FSMContext):
    """ Processing start command. """

    await execute_request_chat(update, bot, fsm_context)
