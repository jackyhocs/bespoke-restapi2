from flask import Flask
from flask_restful import Api, Resource, reqparse
from model import BespokeModel
import sys

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('sweetness', type=int, help='Sweetness must be int')
parser.add_argument('name')


class BespokeApp(Resource):
    def get(self, _id):
        try:
            if BespokeModel.is_valid(_id):
                result = BespokeModel.get_by_id(_id)
                if result is None:
                    fruit = {'_id': _id, 'error': "Entry not retrieved"}
                else:
                    fruit = {'name': result.name, 'sweetness': result.sweetness, '_id': result._id}
            else:
                fruit = {'_id': _id, 'error': "Entry does not exist"}
            return fruit
        except Exception as e:
            return e

    def post(self, _id):
        try:
            if BespokeModel.is_valid(_id):
                args = parser.parse_args()
                sweetness = args['sweetness']
                name = args['name']
                result = BespokeModel.update_item(_id, name, sweetness)
                if result is None:
                    fruit = {'_id': _id, 'error': "Entry not updated"}
                else:
                    fruit = {'name': result.name, 'sweetness': result.sweetness, '_id': result._id}
            else:
                fruit = {'_id': _id, 'error': "Entry does not exist"}
            return fruit
        except Exception as e:
            return e

    def delete(self, _id):
        try:
            if BespokeModel.is_valid(_id):
                result = BespokeModel.delete_item(_id)
                if result is None:
                    fruit = {'_id': _id, 'error': "Entry could not be deleted"}
                else:
                    fruit = {'name': result.name, 'sweetness': result.sweetness, '_id': result._id}
            else:
                fruit = {'_id': _id, 'error': "Entry does not exist"}
            return fruit
        except Exception as e:
            return e


class BespokeNoParamApp(Resource):
    def put(self):
        try:
            args = parser.parse_args()
            sweetness = args['sweetness']
            name = args['name']
            if not BespokeModel.is_existing_name(name):
                result = BespokeModel.insert_item(name, sweetness)
                if result is None:
                    fruit = {'name': name,'sweetness': sweetness, 'error': "Entry does not exist"}
                else:
                    fruit = {'name': result.name, 'sweetness': result.sweetness, '_id': result._id}
                return fruit
            else:
                return None
        except Exception as e:
            return e

    def get(self):
        try:
            result = BespokeModel.get_all()
            json_array = []
            for i in result:
                json_array.append({'name': i.name, 'sweetness': i.sweetness, '_id': i._id})
            return json_array
        except Exception as e:
            return e


api.add_resource(BespokeApp, '/fruits/<_id>')
api.add_resource(BespokeNoParamApp, '/fruits')

if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')
