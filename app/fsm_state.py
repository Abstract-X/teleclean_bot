from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMState(StatesGroup):
    """ General enum for all states. """

    REQUEST_CHAT = State()
