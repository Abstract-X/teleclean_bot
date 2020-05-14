from aiogram import Bot
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from app import resources, FSMState
from app.services import Cleaner


async def execute_hello(update: Message, bot: Bot):
    """ Show greeting to new user. """

    await bot.send_message(
        chat_id=update.from_user.id,
        text=resources.text.HELLO_MESSAGE
    )


async def execute_request_chat(update: Message, bot: Bot, fsm_context: FSMContext):
    """ Request chat information for cleaning. """

    await bot.send_message(
        chat_id=update.from_user.id,
        text=resources.text.REQUEST_CHAT_MESSAGE
    )

    await fsm_context.set_state(FSMState.REQUEST_CHAT)


async def execute_incorrect_chat(update: Message, bot: Bot):
    """ Report that the chat data sent is incorrect. """

    await bot.send_message(
        chat_id=update.from_user.id,
        text=resources.text.INCORRECT_CHAT_MESSAGE,
        reply_to_message_id=update.message_id
    )


async def execute_chat_cleaning(update: Message, bot: Bot, cleaner: Cleaner):
    """ Cleaning chat from all own messages. """

    try:
        chat_data = int(update.text)
    except ValueError:
        chat_data = update.text

    await bot.send_message(
        chat_id=update.from_user.id,
        text=resources.text.CLEANING_STARTED_MESSAGE,
        reply_to_message_id=update.message_id
    )

    report = await cleaner.clear_chat(chat_data)

    await bot.send_message(
        chat_id=update.from_user.id,
        text=resources.text.CLEANING_FINISHED_MESSAGE.format(
            chat_name=report.chat_name,
            chat_id=report.chat_id,
            deleted_amount=report.amount_messages
        ),
        reply_to_message_id=update.message_id
    )
