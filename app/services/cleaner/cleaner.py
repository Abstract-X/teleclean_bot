import asyncio
from asyncio import AbstractEventLoop
from typing import Optional, Union

from telethon import TelegramClient
from telethon.tl.types import Message, Channel, Chat

from .cleaning_report import CleaningReport
from . import exceptions


class Cleaner:
    """ Chat cleaner, allows you to delete all your messages. """

    def __init__(self, session_name: str, app_id: int, app_hash: str, loop: Optional[AbstractEventLoop]):

        if loop is None:
            loop = asyncio.get_event_loop()

        self._loop = loop
        self._client = TelegramClient(session_name, app_id, app_hash, loop=loop)
        self.user_id: Optional[int] = None

    async def connect(self):
        """ Start the TelegramClient (connects and logs in if necessary). """

        # noinspection PyUnresolvedReferences
        await self._client.start()

    async def disconnect(self):
        """ Disconnect from Telegram. """

        await self._client.disconnect()

    async def load_user_id(self):
        """ Loading Telegram user ID. """

        me = await self._client.get_me()
        self.user_id = me.id

        return self.user_id

    async def clear_chat(self, chat_data: Union[int, str]):
        """ Clear chat from all your messages.
            Accepts chat_id or chat_name.
        """

        chat_entity = await self._get_chat_entity(chat_data)

        messages_part = await self._get_chunk_self_messages(chat_entity)
        deleted_amount = 0

        while any((isinstance(message, Message) for message in messages_part)):
            affected_messages = await self._client.delete_messages(
                entity=chat_entity, message_ids=[message.id for message in messages_part],
            )
            deleted_amount += sum([i.pts_count for i in affected_messages])
            messages_part = await self._get_chunk_self_messages(chat_entity)

        return CleaningReport(chat_entity.title, chat_entity.id, deleted_amount)

    async def check_correct_chat_data(self, chat_data: Union[int, str]):
        """ Checking chat data for correctness.
            Accepts chat_id or chat_name.
        """

        try:
            await self._get_chat_entity(chat_data)
            return True
        except exceptions.ChatNotFoundError:
            return False

    async def _get_chat_entity(self, chat_data: Union[int, str]) -> Union[Channel, Chat]:
        """ Getting a chat entity from a list of dialogs.
            Accepts chat_id or chat_name.
        """

        async for dialog in self._client.iter_dialogs():
            entity = dialog.entity
            if (isinstance(entity, Channel) and entity.megagroup) or isinstance(entity, Chat):
                if chat_data in (entity.id, entity.title):
                    return entity
        else:
            raise exceptions.ChatNotFoundError(chat_data)

    async def _get_chunk_self_messages(self, entity: Union[Channel, Chat], limit: int = 3000):
        """ Getting a message chunk (restrictions do not allow you to receive everything at once). """

        return await self._client.get_messages(entity=entity, limit=limit, from_user=self.user_id)
