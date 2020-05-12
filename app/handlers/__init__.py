from aiogram import Dispatcher

from . import none_state, request_chat_state
from app import FSMState
from app.filters import CorrectChatFilter
from app.services import Cleaner


def register_none_state_handlers(dispatcher: Dispatcher, allowed_user_id: int):
    """ Registration handlers without a given state. """

    state = None

    dispatcher.register_message_handler(
        none_state.handle_start_command,
        user_id=allowed_user_id,
        commands=["start"],
        state=state
    )


def register_request_chat_state_handlers(dispatcher: Dispatcher, cleaner: Cleaner):
    """ Registration handlers with a given chat data request state. """

    state = FSMState.REQUEST_CHAT

    dispatcher.register_message_handler(
        request_chat_state.handle_start_command,
        commands=["start"],
        state=state
    )

    dispatcher.register_message_handler(
        request_chat_state.handle_chat_message,
        CorrectChatFilter(cleaner),
        state=state
    )

    dispatcher.register_message_handler(
        request_chat_state.handle_incorrect_chat_message,
        state=state
    )


def register_all(dispatcher: Dispatcher, allowed_user_id: int, cleaner: Cleaner):
    """ Registration of all handlers. """

    register_none_state_handlers(dispatcher, allowed_user_id)
    register_request_chat_state_handlers(dispatcher, cleaner)
