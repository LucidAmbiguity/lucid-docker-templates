"""Routes Module"""
from flask import Blueprint

routes = Blueprint('routes', __name__)
# pylint: disable=wrong-import-position
from .routes import routes  # type: ignore[misc]
