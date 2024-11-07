from flask_restful import Resource

class Cart(Resource):
    def get(self):
        return {'message': 'Hello from get Cart'}
    
    def post(self):
        return {'message': 'Hello from post Cart'}
    
    def put(self):
        return {'message': 'Hello from put Cart'}
    
    def delete(self):
        return {'message': 'Hello from delete Cart'}