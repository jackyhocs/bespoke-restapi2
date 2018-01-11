from pymongo import MongoClient
from bson import ObjectId
from validator import error_builder
import sys


class BespokeDao:
    def __init__(self):
        self._logger = print
        client = MongoClient('mongo')
        self.db = getattr(client, 'fruits')

    def get_all(self):
        db = self.db.fruits
        fruit = db.find()
        items = []
        for i in fruit:
            items.append(i)
        return items

    def get_by_id(self, _id):
        db = self.db.fruits
        result = db.find_one({'_id': ObjectId(_id)})
        print("in dao", file=sys.stderr)
        print(result, file=sys.stderr)
        if not result:
            return None
        return result

    def get_by_name(self, name):
        db = self.db.fruits
        result = db.find_one({'name': name})
        if not result:
            return None
        return result

    def check_if_id_exists(self, _id):
        db = self.db.fruits
        result = db.find_one({'_id': ObjectId(_id)})
        if not result:
            return None
        return result

    def insert_item(self, name, sweetness):
        db = self.db.fruits
        inserted = db.insert_one({'name': name, 'sweetness': sweetness})
        find = db.find_one({'_id': inserted.inserted_id})
        if not find:
            return None
        return find

    def update_item(self, _id, name, sweetness):
        db = self.db.fruits
        modified = db.find_one_and_update({'_id': ObjectId(_id)},
                                 {'$set': {'name': name, 'sweetness': sweetness}})
        if not modified:
            return None
        return modified

    def delete_item(self, _id):
        db = self.db.fruits
        deleted = db.find_one_and_delete({'_id': ObjectId(_id)})
        if not deleted:
            return None
        return deleted
