import logging
from flask import request

from routes.restplus import blockchain_api
from routes.api.parsers import input_args

from flask_restplus import Resource

log = logging.getLogger(__name__)
ns = blockchain_api.namespace(
    'Caps', description='Returns the input but in Caps')


@ns.route('/')
class Caps(Resource):
    """ Take input and return it in Caps"""

    # , text
    @ns.response(200, 'Success')
    @ns.response(400, 'ES error')
    @ns.expect(input_args)
    def get(self):

        data = request.args

        result = {}
        result['Caps'] = data['Text'].upper()
        result['Original'] = data['Text']

        return result
