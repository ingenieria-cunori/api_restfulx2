from flask_restx import Namespace, Resource, fields
from flask import request
from ..services.number_service import NumberService

ns = Namespace('converters', description='Conversiones de datos')

number_model = ns.model('NumberInput', {
    'number': fields.Integer(required=True, description='Número a convertir', min=0, max=9)
})

@ns.route('/to-words')
class NumberToWords(Resource):
    @ns.expect(number_model, validate=True)
    def post(self):
        """Convierte un número entero a su representación en letras"""
        data = request.json
        number = data['number']
                
        words = NumberService.convert_to_words(number)
        
        return {
            'original': number,
            'words': words
        }, 200