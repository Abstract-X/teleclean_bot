from aiogram import Bot, Dispatcher

from .instances import InstancesMiddleware
from app.services import Cleaner


def setup(dispatcher: Dispatcher, bot: Bot, cleaner: Cleaner):
    """ Install middlewares. """

    dispatcher.middleware.setup(InstancesMiddleware(bot, dispatcher, cleaner))
