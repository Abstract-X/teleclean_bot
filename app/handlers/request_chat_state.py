from aiogram import Bot
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from app.executors import execute_chat_cleaning, execute_request_chat, execute_incorrect_chat
from app.services import Cleaner


async def handle_chat_message(update: Message, bot: Bot, fsm_context: FSMContext, cleaner: Cleaner):
    """ Processing sent chat data. """

    task_chat_cleaning = bot.loop.create_task(execute_chat_cleaning(update, bot, cleaner))
    task_request_chat = bot.loop.create_task(execute_request_chat(update, bot, fsm_context))

    await task_request_chat
    await task_chat_cleaning


async def handle_incorrect_chat_message(update: Message, bot: Bot):
    """ Processing sent incorrect chat data. """

    await execute_incorrect_chat(update, bot)
