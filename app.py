from flask import Flask
from flask_restful import Api, Resource
import os

app = Flask(__name__)
api = Api(app)

class sayHello(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(sayHello, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))
