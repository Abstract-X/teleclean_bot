# TeleClean Bot
Bot to remove your messages from Telegram public chats.
**Script does not collect your sensitive data in any way, you can verify this by examining the code.**

## Preparing
You will need:
- Token from the bot with which you will choose a chat for cleaning. To get a token, contact [@BotFather](https://t.me/BotFather).
Token example:
``` text
123456789:AABBCCDDEEFFaabbccddeeff-1234567890
```
- APP_ID and APP_HASH for your account, which will be cleaned. You can get them here: https://my.telegram.org/, in the API Development tools section, create a new application.
APP_ID and APP_HASH examples:
``` text
123456
0123456789abcdef0123456789abcdef
```
- [Python 3.7+](https://www.python.org/downloads/).
- Copy of this repository.
``` shell script
# Download ZIP archive (and unzip):
https://github.com/Abstract-X/teleclean_bot/archive/master.zip

#    OR (!)

# Using Git:
git clone https://github.com/Abstract-X/teleclean_bot.git
```

## Launching
- Install the required libraries for work:
``` python
pip install -r requirements.txt
```
- Create the **.env** file *(teleclean_bot/.env)*, place the following lines in it, substituting the data obtained:
``` text
BOT_TOKEN = ...
TELEGRAM_APP_ID = ...
TELEGRAM_APP_HASH = ...
TELEGRAM_APP_SESSION_NAME = auth
```
- Run using Python:
``` python
python __main__.py
```
- Write to your bot «/start»! ;)
