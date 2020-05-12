from aiogram import Bot, Dispatcher

from .instances import InstancesMiddleware


def setup(dispatcher: Dispatcher, bot: Bot):
    """ Install middlewares. """

    dispatcher.middleware.setup(InstancesMiddleware(bot, dispatcher))
