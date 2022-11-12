"""Basic Extensions for App"""
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
ma = Marshmallow() # type: ignore[misc]
migrate = Migrate() # type: ignore[misc]
bcrypt = Bcrypt() # type: ignore[misc]
cors = CORS() # type: ignore[misc]
