import os

from envparse import env


env_path = f"{os.getcwd()}/.env"
env.read_envfile(path=env_path)

BOT_TOKEN = env.str("BOT_TOKEN")
TELEGRAM_APP_ID = env.int("TELEGRAM_APP_ID")
TELEGRAM_APP_HASH = env.str("TELEGRAM_APP_HASH")
TELEGRAM_APP_SESSION_NAME = env.str("TELEGRAM_APP_SESSION_NAME")
