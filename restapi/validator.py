#import voluptuous
from bson import ObjectId
from voluptuous import Schema, Required, All, Length
import sys
import re

def is_valid_id(_id):
    return True if ObjectId.is_valid(_id) else False

def is_valid_input(name, sweetness):
    try:
        schema = Schema({Required('sweetness'): All(int)})
        schema({'sweetness': sweetness})
        return True if re.match("^[a-zA-Z]+$", name) else False
    except:
        return False
