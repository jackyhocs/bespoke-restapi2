from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from model import BespokeModel

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('sweetness', type=int, help='Sweetness must be int')
parser.add_argument('name')

class BespokeApp(Resource):
    def get(self, name):
        model = BespokeModel()
        result = model.get_by_name(name)
        return result

    def post(self, name):
        model = BespokeModel()
        args = parser.parse_args()
        sweetness = args['sweetness']
        output = model.check_and_update(name, sweetness)
        return output

    def put(self, name):
        model = BespokeModel()
        args = parser.parse_args()
        sweetness = args['sweetness']
        output = model.check_and_insert(name, sweetness)
        return output

    def delete(self, name):
        model = BespokeModel()
        output = model.check_and_delete(name)
        return output

api.add_resource(BespokeApp, '/fruits/<name>')

if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')
