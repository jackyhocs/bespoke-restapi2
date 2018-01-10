from flask import Flask
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
    def get(self, _id):
        try:
            if BespokeModel.is_valid(_id):
                result = BespokeModel.get_by_id(_id)
                return result
            else:
                return None
        except Exception as e:
            return e

    def post(self, _id):
        try:
            if BespokeModel.is_valid(_id):
                args = parser.parse_args()
                sweetness = args['sweetness']
                result = BespokeModel.update_item(_id, sweetness)
                return result
            else:
                return None
        except Exception as e:
            return e

    def delete(self, _id):
        # TODO: change this to ID, and validate the ID is proper
        try:
            if BespokeModel.is_valid(_id):
                result = BespokeModel.delete_item(_id)
                return result
            else:
                return None
        except Exception as e:
            return e


class BespokeMultipleApp(Resource):
    def put(self, _id):
        # TODO: change this to ID, and validate the ID is proper
        try:
            args = parser.parse_args()
            sweetness = args['sweetness']
            name = args['name']
            #TODO: Change the update function
            if not BespokeModel.is_existing_id(_id):
                result = BespokeModel.insert_item(name, sweetness)
                return result
            else:
                return None
        except Exception as e:
            return e

    def get(self):
        try:
            result = BespokeModel.get_all()
            return result
        except Exception as e:
            return e


api.add_resource(BespokeApp, '/fruits/<_id>')
api.add_resource(BespokeMultipleApp, '/fruits')

if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')
