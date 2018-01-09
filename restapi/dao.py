from pymongo import MongoClient
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
            items.append({'name': i['name'], 'sweetness': i['sweetness']})
        return items

    def get_by_name(self, name):
        db = self.db.fruits
        try:
            result = db.find_one({'name': name})
            #print(result, file=sys.stderr)
            if result is None:
                output = {'name': name, 'error': "Item not found in database"}
            else:
                output = {'name': name, 'sweetness': result['sweetness']}
            return output
        except Exception as e:
            print(e, file=sys.stderr)
            output = {'error': "Error"}
            return output

    def check_if_exists(self, name):
        db = self.db.fruits
        try:
            fruit = db.find_one({'name': name})
            if fruit is None:
                return False
            else:
                return True
        except Exception as e:
            print(e, file=sys.stderr)
            output = {'error': "Error, trying to find if an item exists"}
            return output

    def insert_item(self, name, sweetness):
        db = self.db.fruits
        try:
            id = db.insert_one({'name': name, 'sweetness': sweetness})
            if id.acknowledged:
                output = {"name": name, "sweetness": sweetness, "inserted": id.acknowledged}
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
                output = {"name": name, "sweetness": sweetness, "modified": modified.acknowledged}
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
