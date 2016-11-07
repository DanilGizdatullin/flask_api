from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    # app.run()
    app.run(debug=True)

# Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
