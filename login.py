import asyncio
import os
from pathlib import Path

from telethon import TelegramClient

api_id = os.environ["APP_ID"]
api_hash = os.environ["APP_HASH"]
# ---------------------------------------

session_path = str((Path(__file__).parent / "saved_session.session").absolute())

if __name__ == '__main__':
    client = TelegramClient(session_path, api_id, api_hash)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.connect())
    client.start()
