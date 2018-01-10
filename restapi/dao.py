from pymongo import MongoClient
from bson import ObjectId
import sys

class BespokeDao:
    def __init__(self):
        self._logger = print
        client = MongoClient('mongo')
        self.db = getattr(client,'fruits')

    def get_all(self):
        db = self.db.fruits
        fruit = db.find()
        items = []
        for i in fruit:
            # TODO: just append the entire fruit data from the DB
            # TODO: let the model decide what information it requires
            items.append({'name': i['name'], 'sweetness': i['sweetness']})
        return items

    def get_by_name(self, name):
        db = self.db.fruits
        try:
            result = db.find_one({'name': name})
            #print(result, file=sys.stderr)
            
             # TODO: just return the fruit data, let the model decide what information it requires (implement this for all of below)
             # TODO: if result is None, return None (implement this for all of the below)
            if result is None:
                output = {'name': name, 'error': "Item not found in database"}
            else:
                output = {'name': name, 'sweetness': result['sweetness'], '_id':i['_id']}
            return output
        except Exception as e:
            print(e, file=sys.stderr)
            output = {'error': "Error"}
            
            # TODO: just log the error and raise the exception (implement this for all of the below)
            return output

    def get_by_id(self, _id):
        db = self.db.fruits
        try:
            result = db.find_one({'_id': ObjectId(_id)})
            # print(result, file=sys.stderr)
            '''if result is None:
                output = {'name': name, 'error': "Item not found in database"}
            else:
                output = result'''
            return result
        except Exception as e:
            print(e, file=sys.stderr)
            output = {'error': "Error, could not find item with id {}".format(_id)}
            return output

    def check_if_id_exists(self, _id):
        db = self.db.fruits
        try:
            result = db.find_one({'_id': ObjectId(_id)})
            return result is not None
        except Exception as e:
            print(e, file=sys.stderr)
            output = {'error': "Error, could not check if item with id {} exists".format(_id)}
            return output

    def check_if_exists(self, name):
        db = self.db.fruits
        try:
            fruit = db.find_one({'name': name})
            return fruit is not None
        except Exception as e:
            print(e, file=sys.stderr)
            output = {'error': "Error, trying to find if an item exists"}
            return output

    def insert_item(self, name, sweetness):
        db = self.db.fruits
        try:
            id = db.insert_one({'name': name, 'sweetness': sweetness})
            if id.acknowledged:
                output = {"name": name, "sweetness": sweetness, "inserted": id.acknowledged,"_id": str(id.inserted_id)}
            else:
                output = {"name": name, "sweetness": sweetness, "error": "Error, occurred when insertin"}
            return output
        except Exception as e:
            print(e, file=sys.stderr)
            output = {'error': "Error, could not insert item"}
            return output

    def update_item(self, name, sweetness):
        db = self.db.fruits
        try:
            modified = db.update_one({'name': name}, {'$set': {'sweetness': sweetness}})
            #print(modified.acknowledged, file=sys.stderr)
            if modified.acknowledged:
                output = {"name": name, "sweetness": sweetness, "modified": modified.acknowledged, "_id": str(modified.upserted_id)}
            else:
                output = {"name":name, "error": "Error, update not acknowledged"}
            return output
        except Exception as e:
            print(e, file=sys.stderr)
            output = {'error': "Error, could not update item"}
            return output

    def delete_item(self, name):
        db = self.db.fruits
        try:
            deleted = db.delete_one({'name': name})
            if deleted.acknowledged:
                output = {"name": name, "deleted": deleted.acknowledged}
            else:
                output = {"name": name, "error": "Error, delete not acknowledged"}
            return output
        except Exception as e:
            print(e, file=sys.stderr)
            output = {'error': "Error, could not perform delete item"}
            return output
