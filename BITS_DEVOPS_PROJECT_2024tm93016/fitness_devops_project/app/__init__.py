from flask import Flask

def create_app(test_config: dict | None = None) -> Flask:
    app = Flask(__name__)
    app.config.update(
        APP_NAME="ACEest_Fitness",
        ENV="production",
    )
    if test_config:
        app.config.update(test_config)

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
