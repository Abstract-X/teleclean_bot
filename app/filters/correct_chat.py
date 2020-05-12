from aiogram.dispatcher.filters import Filter

from app.services import Cleaner


class CorrectChatFilter(Filter):
    """ Checking the sent chat data for correctness. """

    def __init__(self, cleaner: Cleaner):

        self.cleaner = cleaner

    async def check(self, update) -> bool:

        try:
            chat_data = int(update.text)
        except ValueError:
            chat_data = update.text

        return await self.cleaner.check_correct_chat_data(chat_data)
