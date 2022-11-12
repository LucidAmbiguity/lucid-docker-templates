"""Main App Module"""
import json
import os
from werkzeug.exceptions import HTTPException, MethodNotAllowed
from werkzeug.sansio.response import Response
from flask import Flask

from config import Config

from .app_types.types import RespObj
from .extensions import db, ma, migrate, bcrypt, cors
import logging


# Creating the application factory


def create_app(test_config: str=None) -> Flask:
    logging.info('Server Started')

    # app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__)

    if test_config is None:
        app.config.from_object(Config)
    else:
        from config import TestConfig  # pylint: disable=import-outside-toplevel
        app.config.from_object(TestConfig)

    try:
        os.makedirs(app.instance_path)
        os.makedirs(f'{app.instance_path}/data')
    except OSError:
        pass

    # # Initialization of extension instances
    db.init_app(app) # type: ignore[misc]
    ma.init_app(app) # type: ignore[misc]
    migrate.init_app(app, db) # type: ignore[misc]
    bcrypt.init_app(app) # type: ignore[misc]
    cors.init_app(app, supports_credentials=True) # type: ignore[misc]

    # # Register the blueprints
    # pylint: disable=import-outside-toplevel
    from .routes import routes
    app.register_blueprint(routes, url_prefix='')

    # pylint: enable=import-outside-toplevel

    @app.errorhandler(HTTPException) # type: ignore[misc]
    def handle_exception_http_exception(exception:HTTPException)->Response:
        """Return JSON instead of HTML for HTTP errors."""
        # start with the correct headers and status code from the error
        response = exception.get_response()
        print('type(response)',type(response))
        print('exception)',type(exception))
        # replace the body with JSON
        resp_obj: RespObj = {
            'status': 'error',
            'code': exception.code,
            'messages': [{
                'code': exception.code,
                'text': exception.name,
            }],
            'result': {'description': exception.description}
        }
        response.data = json.dumps(resp_obj) # type: ignore[attr-defined,misc]
        response.content_type = 'application/json'
        return response

    @app.errorhandler(MethodNotAllowed) # type: ignore[misc]
    def handle_exception_method_not_allowed(exception:MethodNotAllowed)->Response: # pylint: disable=line-too-long
        """Return JSON instead of HTML for HTTP errors."""
        print('handle_exception_method_not_allowed')
        # start with the correct headers and status code from the error
        response = exception.get_response()
        # replace the body with JSON
        resp_obj: RespObj = {
            'status': 'error',
            'code': exception.code,
            'messages': [{
                'code': exception.code,
                'text': exception.name,
            }],
            'result': {'description': exception.description}
        }
        response.data = json.dumps(resp_obj) # type: ignore[attr-defined,misc]
        response.content_type = 'application/json'
        return response

    return app
