from dao import BespokeDao
from flask_restful import Resource, reqparse
from flask import jsonify, request
import sys

parser = reqparse.RequestParser()
parser.add_argument('sweetness', type=int, help='Sweetness must be int')
parser.add_argument('name')

class BespokeModel(Resource):
    '''def __init__(self, collection):
        self.id = collection['id'] if 'id' in collection else None
        self.name = collection['name'] if 'name' in collection else None
        self.sweetness = collection['sweetness'] if 'sweetness' in collection else None
    '''
    def get_by_name(self, name):
        db = BespokeDao()
        try:
            #print("In model", file=sys.stderr)
            item = db.get_by_name(name)
            return item

        except Exception as e:
            print(e, file=sys.stderr)
            return {'name': name, 'error': e}

    def check_and_update(self, name, sweetness):
        db = BespokeDao()
        if db.check_if_exists(name):
            output = db.update_item(name, sweetness)
        else:
            output = {'error': "Cannot perform POST request on non-existent entry"}
        return output

    def check_and_insert(self, name, sweetness):
        db = BespokeDao()
        if db.check_if_exists(name):
            output = db.update_item(name, sweetness)
        else:
            output = db.insert_item(name, sweetness)
        return output

    def check_and_delete(self, name):
        db = BespokeDao()
        if db.check_if_exists(name):
            output = db.delete_item(name)
        else:
            output = {'error': "Cannot perform DELETE request on non-existent entry"}
        return output