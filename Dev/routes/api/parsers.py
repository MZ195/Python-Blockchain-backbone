from flask_restplus import reqparse

input_args = reqparse.RequestParser()
input_args.add_argument('Text', type=str, required=True,
                        help='Input to be returned')
