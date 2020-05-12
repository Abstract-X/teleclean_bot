from aiogram import Bot
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from app import resources, FSMState


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
