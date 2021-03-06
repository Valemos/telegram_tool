import argparse
import csv
import datetime
import json
import os
import time
from pathlib import Path
import random

from colorama import Fore
from telethon import TelegramClient

from login import session_path


is_config_required = "APP_CONFIG" not in os.environ


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--Session", default=session_path,
                    help='Session file generated by login script eg. "saved_session.session"')
parser.add_argument("-t", "--Timeout", default=10,
                    help="Delay between messages sent in minutes")
parser.add_argument("-c", "--Config", required=is_config_required,
                    help='path to json file with list of channels with key "targets"'
                         ' and list of messages with key "messages"')
args = parser.parse_args()

api_id = os.environ["APP_ID"]
api_hash = os.environ["APP_HASH"]

if is_config_required:
    with Path(args.Config).open() as f:
        config_raw = f.read()
else:
    config_raw = os.environ["APP_CONFIG"]

config = json.loads(config_raw)
targets = config["targets"]
messages = config["messages"]

time_from_arg = args.Timeout
sleep_time = int(time_from_arg) * 60

client = TelegramClient(session_path, api_id, api_hash)
client.start()
# ---------------------------------------

print(Fore.RED + f'Spammer will send message each {time_from_arg} minutes')


while True:
    for target in targets:
        message_selected = random.choice(messages)
        client.send_message(target, message_selected)
        print(Fore.GREEN + f"message was sent to {target} "
                           f"in {datetime.datetime.now()}")
    print(Fore.GREEN + f"Sleep {time_from_arg} minutes")
    time.sleep(sleep_time)
