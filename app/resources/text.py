# noinspection PyUnresolvedReferences
from aiogram.utils.markdown import (
    hbold as b,            # <b>...</b>
    hitalic as i,          # <i>...</i>
    hpre as pre,           # <pre>...</pre>
    hcode as code,         # <code>...</code>
    hlink as link,         # <a href="{link}">...</a>
    hide_link,             # <a href="{link}">&#8203;</a>
    hstrikethrough as s,   # <s>...</s>
    hunderline as u        # <u>...</u>
)


HELLO_MESSAGE = """👋🏼 TeleClean Bot welcomes you!"""
REQUEST_CHAT_MESSAGE = f"""🆔 Send me {code('chat_id')} or {code('chat_name')} for cleaning."""
INCORRECT_CHAT_MESSAGE = f"""♻️ I can't find a chat with this name and ID, please check the data and try again."""
CLEANING_STARTED_MESSAGE = f"""🧹 Cleaning started!"""
CLEANING_FINISH_MESSAGE = f"""✅ {b('Cleaning completed!')}

{b('Chat name:')} {'{chat_name}'}
{b('Chat ID:')}   {'{chat_id}'}
{b('Deleted:')}   {'{deleted_amount}'}"""
