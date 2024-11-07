from flask_restful import Resource

class Order(Resource):
    def get(self):
        return {'message': 'Hello from get Order'}
    
    def post(self):
        return {'message': 'Hello from post Order'}
    
    def put(self):
        return {'message': 'Hello from put Order'}
    
    def delete(self):
        return {'message': 'Hello from delete Order'}