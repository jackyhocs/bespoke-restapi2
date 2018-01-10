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
        model = BespokeModel()
        result = model.get_by_name(name)
        return result

    def post(self, name):
        # TODO: post should exist in another class within this file
        # TODO: one class deals with a single entity while the other deals with a collection of entities
        # TODO: post does not take any parameters though, it just takes a payload
        model = BespokeModel()
        args = parser.parse_args()
        sweetness = args['sweetness']
        output = model.check_and_update(name, sweetness)
        return output

    def put(self, name):
        # TODO: change this to ID, and validate the ID is proper
        model = BespokeModel()
        args = parser.parse_args()
        sweetness = args['sweetness']
        output = model.check_and_insert(name, sweetness)
        return output

    def delete(self, name):
        # TODO: change this to ID, and validate the ID is proper
        model = BespokeModel()
        output = model.check_and_delete(name)
        return output

api.add_resource(BespokeApp, '/fruits/<name>')

if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')
