from flask import Flask, make_response, jsonify
from flask_restful import Api, Resource, reqparse
from model import BespokeModel
import sys
from validator import is_valid_id, is_valid_input

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('sweetness', type=int, help='Sweetness must be int')
parser.add_argument('name')


class BespokeApp(Resource):
    def get(self, _id):
        try:
            if is_valid_id(_id):
                result = BespokeModel.get_by_id(_id)
                if result is None:
                    fruit = {'_id': _id, 'error': "Entry not retrieved"}
                else:
                    fruit = {'name': result.name, 'sweetness': result.sweetness, '_id': result._id, 'retrieved': True}
                return fruit
            else:
                return make_response(jsonify({"error": 'ID specified does not exist'}), 404)

        except:
            return make_response(jsonify({"error": 'Unable to retrieve item'}), 500)

    def post(self, _id):
        try:
            if is_valid_id(_id):
                args = parser.parse_args()
                sweetness = args['sweetness']
                name = args['name'].strip()
                name = " ".join(name.split())
                if name is not None and sweetness is not None and is_valid_input(name, sweetness):
                    if not BespokeModel.is_existing_name(name):
                        result = BespokeModel.update_item(_id, name, sweetness)
                        if result is None:
                            fruit = {'_id': _id, 'error': "Entry not updated"}
                        else:
                            fruit = {'name': result.name, 'sweetness': result.sweetness, '_id': result._id, 'updated': True}
                        return fruit
                    else:
                        return make_response(jsonify({'error': 'Fruit with same name already exists, update denied'}), 404)
                else:
                    return make_response(jsonify({'error': 'Parameters provided are invalid'}), 404)
            else:
                return make_response(jsonify({"error": 'ID specified does not exist'}), 404)
        except:
            return make_response(jsonify({"error": 'Unable to update item'}), 500)

    def delete(self, _id):
        try:
            if is_valid_id(_id):
                result = BespokeModel.delete_item(_id)
                if result is None:
                    fruit = {'_id': _id, 'error': "Entry could not be deleted"}
                else:
                    fruit = {'name': result.name, 'sweetness': result.sweetness, '_id': result._id, 'deleted': True}
                return fruit
            else:
                return make_response(jsonify({"error": 'ID specified does not exist'}), 404)
        except:
            return make_response(jsonify({"error": 'Unable to delete item'}), 500)


class BespokeNoParamApp(Resource):
    def put(self):
        try:
            args = parser.parse_args()
            sweetness = args['sweetness']
            name = args['name'].strip()
            name = " ".join(name.split())
            if name is not None and sweetness is not None and is_valid_input(name, sweetness):
                if not BespokeModel.is_existing_name(name):
                    result = BespokeModel.insert_item(name, sweetness)
                    if result is None:
                        fruit = {'name': name, 'sweetness': sweetness, 'error': "Entry does not exist"}
                    else:
                        fruit = {'name': result.name, 'sweetness': result.sweetness, '_id': result._id, 'inserted': True}
                    return fruit
                else:
                    return make_response(jsonify({"error": 'Duplicate fruits not accepted'}), 404)
            else:
                return make_response(jsonify({'error': 'Parameters provided are invalid'}), 404)
        except:
            return make_response(jsonify({"error": 'Unable to insert item'}), 500)

    def get(self):
        try:
            result = BespokeModel.get_all()
            json_array = []
            for i in result:
                json_array.append({'name': i.name, 'sweetness': i.sweetness, '_id': i._id})
            return json_array
        except:
            return make_response(jsonify({"error": 'Unable to get all items'}), 500)


api.add_resource(BespokeApp, '/fruits/<_id>')
api.add_resource(BespokeNoParamApp, '/fruits')

if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')
