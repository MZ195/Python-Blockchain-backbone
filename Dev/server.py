import logging.config

import cherrypy
from paste.translogger import TransLogger
from flask import Flask, Blueprint
from flask_cors import CORS

from routes.api.endpoints.Blockchain import ns as caps_namespace
from routes.restplus import blockchain_api

import settings
from modules import Blockchain

app = Flask(__name__)
CORS(app)
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.debug = settings.FLASK_DEBUG

def initialize_app(flask_app):
    configure_app(flask_app)

    # prepare a blueprint
    blueprint = Blueprint('Blockchain', __name__, url_prefix='/api')
    blockchain_api.init_app(blueprint)

    blockchain_api.add_namespace(caps_namespace)

    flask_app.register_blueprint(blueprint)


def run_server():
    # Enable WSGI access logging via Paste
    app_logged = TransLogger(app)
    # Mount the WSGI callable object (app) on the root directory
    cherrypy.tree.graft(app_logged, '/')
    # Set the configuration of the web server
    cherrypy.config.update({
        'engine.autoreload.on': settings.ENGINE_AUTO_RELOAD,
        'log.screen': settings.LOG_SCREEN,
        'server.socket_host': settings.SERVER_NAME,
        'server.socket_port': settings.SERVER_PORT,
        'server.thread_pool': 30,
    })

    # Start the CherryPy WSGI web server
    cherrypy.engine.start()
    cherrypy.engine.block()


def main():
    initialize_app(app)
    print('>>>>> Starting development server at http://{}:{}/api/ <<<<<'.format(settings.SERVER_NAME,
                                                                                   settings.SERVER_PORT))
    run_server()


if __name__ == "__main__":
    main()
