from flask_restx import Api
from .converter import ns as converter_ns

api = Api(title='ApiRestX', version='1.0')
api.add_namespace(converter_ns, path='/convert')