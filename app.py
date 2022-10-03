from flask import Flask
from flask_smorest import Api
from resources.item import itm as ItemBluPrint
from resources.store import blp as StoreBluPrint
from resources.tag import tg as TagBluePrint

import os
from db import db

def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPAGATE_EXCEPTIONS"] = True 
    app.config["API_TITLE"] = "Store Rest API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"]= "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config ["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # with app.app_context():
    #     db.create_all()

    app.before_first_request
    def create_tables():
        db.create_all()
    api = Api(app)

    api.register_blueprint(ItemBluPrint)
    api.register_blueprint(StoreBluPrint)
    app.register_blueprint(TagBluePrint)

    return app
