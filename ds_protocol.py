# Trevor Walker
# Walkertk@uci.edu
# 35049080

import json
from collections import namedtuple

# Namedtuple to hold the values retrieved from json messages.

DataTuple = namedtuple('response', ['type','message', 'token'])


def extract_json(json_msg: str) -> DataTuple:

    try:
        json_obj = json.loads(json_msg)
        response = json_obj['response']
        type = response['type']
        message = response['message']
        try:
            token = response['token']
        except:
            token = ''
    except json.JSONDecodeError:
        print("Json cannot be decoded.")

    return DataTuple(type, message, token)
