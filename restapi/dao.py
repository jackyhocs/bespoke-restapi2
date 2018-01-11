from pymongo import MongoClient
from bson import ObjectId
import sys


class BespokeDao:
    def __init__(self):
        self._logger = print
        client = MongoClient('mongo')
        self.db = getattr(client, 'fruits')

    def get_all(self):
        try:
            db = self.db.fruits
            fruit = db.find()
            items = []
            for i in fruit:
                items.append(i)
            return items
        except Exception as e:
            print(e, file=sys.stderr)
            raise

    def get_by_id(self, _id):
        try:
            db = self.db.fruits
            result = db.find_one({'_id': ObjectId(_id)})
            return result if result is not None else None
        except Exception as e:
            print(e, file=sys.stderr)
            raise

    def get_by_name(self, name):
        try:
            db = self.db.fruits
            result = db.find_one({'name': name})
            return result if result is not None else None
        except Exception as e:
            print(e, file=sys.stderr)
            raise

    def check_if_id_exists(self, _id):
        try:
            db = self.db.fruits
            result = db.find_one({'_id': ObjectId(_id)})
            return result if result is not None else None
        except Exception as e:
            print(e, file=sys.stderr)
            raise

    def insert_item(self, name, sweetness):
        try:
            db = self.db.fruits
            inserted = db.insert_one({'name': name, 'sweetness': sweetness})
            find = db.find_one({'_id': inserted.inserted_id})
            return find if find is not None else None
        except Exception as e:
            print(e, file=sys.stderr)
            raise

    def update_item(self, _id, name, sweetness):
        try:
            db = self.db.fruits
            modified = db.update_one({'_id': ObjectId(_id)},
                                     {'$set': {'name': name, 'sweetness': sweetness}})
            if modified.modified_count == 1:
                return {'name': name, 'sweetness': sweetness, '_id': _id}
            else:
                return None
        except Exception as e:
            print(e, file=sys.stderr)
            raise

    def delete_item(self, _id):
        try:
            db = self.db.fruits
            deleted = db.find_one_and_delete({'_id': ObjectId(_id)})
            return deleted if deleted is not None else None
        except Exception as e:
            print(e, file=sys.stderr)
            raise
