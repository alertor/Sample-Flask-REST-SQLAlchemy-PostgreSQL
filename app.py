from flask import Flask
from flask_restful import Api

from resources import Spot, SpotList

app = Flask(__name__)
api = Api(app)

api.add_resource(SpotList, '/spots')
api.add_resource(Spot, '/spots/<int:spot_id>')

if __name__ == '__main__':
    app.run(debug=True)