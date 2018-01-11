from bson import ObjectId
from voluptuous import Schema, Required, All
import re
import sys

def is_valid_id(_id):
    return True if ObjectId.is_valid(_id) else False


def error_builder(_id=None, msg=None, exception=None, collection=None):
    error = {}
    print(error, file=sys.stderr)
    if _id:
        error['_id'] = _id
    print(error, file=sys.stderr)
    if collection:
        for k, v in collection:
            error[k] = v
    print(error, file=sys.stderr)
    if msg:
        error['msg'] = msg
    print(error, file=sys.stderr)
    if exception:
        error['exception'] = str(exception)
    print(error, file=sys.stderr)
    return error


def is_valid_input(name, sweetness):
    try:
        schema = Schema({Required('sweetness'): All(int)})
        schema({'sweetness': sweetness})
        return True if re.match("^[a-zA-Z ]+$", name) else False
    except:
        return False


def sanitize_input(user_input):
    if not user_input:
        return None
    sanitized = " ".join(user_input.strip().split())
    return sanitized
