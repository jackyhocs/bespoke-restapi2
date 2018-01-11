from flask import Flask, make_response, jsonify
from flask_restful import Api, Resource, reqparse
from model import BespokeModel
import sys
from validator import is_valid_id, is_valid_input, error_builder, sanitize_input

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('sweetness', type=int, help='Sweetness must be int')
parser.add_argument('name')


class BespokeApp(Resource):
    def get(self, _id):
        if not is_valid_id(_id):
            error = error_builder(_id, "Invalid ID entered")
            return make_response(jsonify(error), 400)

        fruit = None
        try:
            result = BespokeModel.get_by_id(_id)
            if result:
                fruit = {'name': result.name,
                         'sweetness': result.sweetness,
                         '_id': result._id,
                         'retrieved': True}
        except Exception as e:
            error = error_builder(_id, "Error when retrieving fruit", e)
            return make_response(jsonify(error), 500)

        if not fruit:
            error = error_builder(_id, "Unable to retrieve fruit")
            return make_response(jsonify(error), 404)

        return make_response(jsonify(fruit), 200)

    def post(self, _id):
        if not is_valid_id(_id):
            error = error_builder(_id, "Invalid ID entered")
            return make_response(jsonify(error), 400)

        args = parser.parse_args()
        sweetness = args['sweetness']
        name = sanitize_input(args['name'])

        if not is_valid_input(name, sweetness):
            error = error_builder(None, "Invalid parameters given, could not create entry")
            return make_response(jsonify(error), 400)

        fruit = None
        try:
            result = BespokeModel.update_item(_id, name, sweetness)
            if result:
                fruit = {'name': result.name,
                         'sweetness': result.sweetness,
                         '_id': result._id,
                         'updated': True}
        except Exception as e:
            error = error_builder(None, "Error while updating fruit", e)
            return make_response(jsonify(error), 500)

        if not fruit:
            error = error_builder(None, "Unable to update fruit")
            return make_response(jsonify(error), 404)

        return make_response(jsonify(fruit), 200)


    def delete(self, _id):
        if not is_valid_id(_id):
            error = error_builder(_id, "Invalid ID entered")
            return make_response(jsonify(error), 400)
        fruit = None
        try:
            result = BespokeModel.delete_item(_id)
            if result:
                fruit = {'name': result.name,
                         'sweetness': result.sweetness,
                         '_id': result._id,
                         'deleted': True}
        except Exception as e:
            error = error_builder(_id, "Error while deleting fruit", e)
            return make_response(jsonify(error), 500)

        if not fruit:
            error = error_builder(_id, "Unable to delete fruit")
            return make_response(jsonify(error), 404)

        return make_response(jsonify(fruit), 200)


class BespokeNoParamApp(Resource):
    def put(self):
        args = parser.parse_args()
        sweetness = args['sweetness']
        name = sanitize_input(args['name'])
        if not is_valid_input(name, sweetness):
            error = error_builder(None, "Invalid parameters given, could not create entry")
            return make_response(jsonify(error), 400)
        fruit = None
        try:
            result = BespokeModel.insert_item(name, sweetness)
            if result:
                fruit = {'name': result.name,
                         'sweetness': result.sweetness,
                         '_id': result._id,
                         'inserted': True}
        except Exception as e:
            error = error_builder(None, "Error while inserting fruit", e)
            return make_response(jsonify(error), 500)

        if not fruit:
            error = error_builder(None, "Unable to insert fruit")
            return make_response(jsonify(error), 404)

        return make_response(jsonify(fruit), 200)

    def get(self):
        try:
            result = BespokeModel.get_all()
        except Exception as e:
            error = error_builder(None, "Unable to retrieve all items", e)
            return make_response(error, 500)
        json_array = []
        for i in result:
            json_array.append({'name': i.name, 'sweetness': i.sweetness, '_id': i._id})
        return json_array


api.add_resource(BespokeApp, '/fruits/<_id>')
api.add_resource(BespokeNoParamApp, '/fruits')

if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')
