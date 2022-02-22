import json
from collections import namedtuple



DataTuple = namedtuple('response', ['type','message', 'token'])

# takes the json message and breaks it back down to a named tuple for easier use

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
