from flask import Flask, jsonify
from flask_cors import CORS
from api.routes import register_routes
from api.error_handler import register_error_handlers
from api.swagger import spec
from flasgger import Swagger

def create_app():
    app = Flask(__name__)

    # CORS
    CORS(app)

    # Dang ki routes
    register_routes(app)

    # Dang ki error handler
    register_error_handlers(app)

    # Swagger UI config
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/swagger.json',
                "rule_filter": lambda rule: True,  # all endpoints
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs/"
    }
    Swagger(app, config=swagger_config, template=spec.to_dict())

    @app.route("/swagger.json")
    def swagger_json():
        return jsonify(spec.to_dict())

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)