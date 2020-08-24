import socket

# Server settings
SERVER_NAME = socket.gethostname()
SERVER_PORT = 9090
ENGINE_AUTO_RELOAD = True
LOG_SCREEN = True

# Flask settings
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False
