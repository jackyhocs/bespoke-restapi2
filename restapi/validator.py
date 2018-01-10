from bson import ObjectId


def is_valid_id(_id):
    return True if ObjectId.is_valid(_id) else False
