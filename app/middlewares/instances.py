from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import Bot, Dispatcher


class InstancesMiddleware(BaseMiddleware):
    """ Middleware to add instances to handler signatures. """

    def __init__(self, bot: Bot, dispatcher: Dispatcher):

        super().__init__()
        self.bot = bot
        self.dispatcher = dispatcher

    async def on_process_message(self, _, data: dict):

        data["bot"] = self.bot
        data["dispatcher"] = self.dispatcher
        data["fsm_context"] = data["state"]
