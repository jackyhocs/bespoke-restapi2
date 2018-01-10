from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from model import BespokeModel

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('sweetness', type=int, help='Sweetness must be int')
parser.add_argument('name')

# TODO: all of the model calls should be wrapped within a try/except block.
# TODO: if an exception happens within the request we want to be able to log it, handle it, and return the error gracefully


class BespokeApp(Resource):
    # TODO: change this to ID, and validate the ID is proper
    def get(self, name):
        try:
            model = BespokeModel()
            result = model.get_by_name(name)
            return result
        except Exception as e:
            return e

    def put(self, name):
        # TODO: change this to ID, and validate the ID is proper
        try:
            model = BespokeModel()
            args = parser.parse_args()
            sweetness = args['sweetness']
            output = model.check_and_insert(name, sweetness)
            return output
        except Exception as e:
            return e

    def delete(self, name):
        # TODO: change this to ID, and validate the ID is proper
        try:
            model = BespokeModel()
            output = model.check_and_delete(name)
            return output
        except Exception as e:
            return e


class BespokeMultipleApp(Resource):
    def post(self):
        try:
            model = BespokeModel()
            args = parser.parse_args()
            sweetness = args['sweetness']
            name = args['name']
            output = model.check_and_update(name, sweetness)
            return output
        except Exception as e:
            return e

    def get(self):
        try:
            model = BespokeModel()
            output = model.get_all()
            return output
        except Exception as e:
            return e


api.add_resource(BespokeApp, '/fruits/<_id>')
api.add_resource(BespokeMultipleApp, '/fruits')

if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')
