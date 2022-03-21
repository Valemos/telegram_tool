import argparse
import csv
import datetime
import time
from pathlib import Path

from colorama import Fore
from telethon import TelegramClient

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--Session", help="Use session file ex: saved_session")
parser.add_argument("-t", "--Timeout", help="Set timeout in minutes")
parser.add_argument("-l", "--List", help="List of channels and messages")
args = parser.parse_args()

api_id = '1074602'
api_hash = '6f99d9b0228563645df01af47f2fb038'
# ---------------------------------------
target = dict()
listFile = csv.reader(open(args.List, 'r'))
for line in listFile:
    key, val = line
    target[key] = val

time_from_arg = args.Timeout
sleep_time = int(time_from_arg) * 60

session_name = str(args.Session) + ".session"
path = Path("__file__").parent / session_name

client = TelegramClient(path, api_id, api_hash)
client.start()
# ---------------------------------------

print(Fore.RED + f'Spammer will send message each {time_from_arg} minutes')

while True:
    for key, value in target.items():
        client.send_message(key, value)
        print(Fore.GREEN + f"{value} was sent to {key} in {datetime.datetime.now()}")
    print(Fore.GREEN + f"Sleep {time_from_arg} minutes")
    time.sleep(sleep_time)
