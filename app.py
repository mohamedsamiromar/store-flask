from flask import Flask
from flask_smorest import Api
from resorces.item import itm as ItemBluPrint
from resorces.store import blp as StoreBluPrint

app = Flask(__name__)
app.config["PROPAGATE_EXCEPTIONS"] = True 
app.config["API_TITLE"] = "Store Rest API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"]= "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


api = Api(app)

api.register_blueprint(ItemBluPrint)
api.register_blueprint(StoreBluPrint)