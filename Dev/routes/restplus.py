import logging
import settings
from flask_restplus import Api

log = logging.getLogger(__name__)


blockchain_api = Api(version='1.0', title='Block-Chain API',
                     description='API template')


@blockchain_api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    if settings.FLASK_DEBUG:
        log.exception(e)
    return {'message': message.strip()}, 500
