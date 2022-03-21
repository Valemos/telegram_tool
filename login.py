import os
from pathlib import Path

from telethon import TelegramClient

api_id = os.environ["APP_ID"]
api_hash = os.environ["APP_HASH"]
# ---------------------------------------

path = Path("__file__").parent / "saved_session.session"

client = TelegramClient(path, api_id, api_hash)
client.connect()
client.start()
