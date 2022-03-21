import json
from pathlib import Path

import random

# specify file with large text that fits in RAM
messages_amount = 10
text_path = Path("lorem_ipsum.txt")

with text_path.open() as f:
    text = f.read()


def generate_message(_text, min_length=10):
    start = random.randint(0, len(_text) - min_length - 1)
    end = random.randint(start + min_length, len(_text) - 1)

    start = get_nearest_delimiter(_text, start, direction=1) + 1
    end = get_nearest_delimiter(_text, end, direction=-1) + 1

    return _text[start:end].replace('\n', '')


def get_nearest_delimiter(_text, index, direction=1, delimiters=" ,:;?!-"):
    # go to the closest space
    while _text[index] not in delimiters:
        index += direction
    # skip all consecutive delimiters
    while _text[index] in delimiters:
        index += direction
    return index


messages = (generate_message(text) for _ in range(messages_amount))

default_config_path = Path("config.json")
with default_config_path.open('r+') as f:
    config = json.load(f)

config["messages"].extend(messages)

with default_config_path.open('w+') as f:
    json.dump(config, f)
