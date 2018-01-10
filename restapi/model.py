from dao import BespokeDao
from flask_restful import Resource, reqparse
from flask import jsonify, request
import sys

# TODO: not needed, only required in the app
parser = reqparse.RequestParser()
parser.add_argument('sweetness', type=int, help='Sweetness must be int')
parser.add_argument('name')

# TODO: remove this Resource extension
class BespokeModel(Resource):
    # TODO: why is this commented out? this is proper structure
    '''def __init__(self, collection):
        self.id = collection['id'] if 'id' in collection else None
        self.name = collection['name'] if 'name' in collection else None
        self.sweetness = collection['sweetness'] if 'sweetness' in collection else None
    '''
    #TODO: add a method to get_by_id(self, _id)
    
    
    
    def get_by_name(self, name):
        db = BespokeDao()
        try:
            #print("In model", file=sys.stderr)
            item = db.get_by_name(name)
            return item

        except Exception as e:
            print(e, file=sys.stderr)
            
            # TODO: raise the exception, have the APP handle it
            return {'name': name, 'error': e}

    # TODO: too much logic here, the model simply tells the dao to update a record and return an instance of itself
    # TODO: the dao will handle how the update needs to happen depending on the data source it is using
    def check_and_update(self, name, sweetness):
        db = BespokeDao()
        if db.check_if_exists(name):
            output = db.update_item(name, sweetness)
        else:
            # TODO: post request ? updates are PUT
            output = {'error': "Cannot perform POST request on non-existent entry"}
        return output

    # TODO: too much logic with these "check and do something" methods, simply call the dao to create a new record
    # TODO: and then either return an instance of itself, or None
    def check_and_insert(self, name, sweetness):
        db = BespokeDao()
        if db.check_if_exists(name):
            output = db.update_item(name, sweetness)
        else:
            output = db.insert_item(name, sweetness)
        return output

    # TODO: too much logic with these "check and do something" methods, simply call the dao to delete a record
    # TODO: and then either return an acknowledgment, or None
    def check_and_delete(self, name):
        db = BespokeDao()
        if db.check_if_exists(name):
            output = db.delete_item(name)
        else:
            output = {'error': "Cannot perform DELETE request on non-existent entry"}
        return output
