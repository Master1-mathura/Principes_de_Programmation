# Import du framework flask
from flask import Flask
from flask_restful import Resource, Api

# Instantiation de l'application
app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        return {
            'products': ['Ipad pro 14', 'MacBook pro', 'Remarkable pro', 'Ordinateur de bureau']
        }

# Définition d'une route
api.add_resource(Product, '/')

# Exécution de l'application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)