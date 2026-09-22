from flask import Flask
from utils.constants import SECRET_KEY, APP_NAME
from database.schema import init_db
from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.train_routes import train_bp
from routes.report_routes import report_bp
from routes.simulation_routes import sim_bp
from routes.emergency_routes import emergency_bp


def create_app() -> Flask:
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.secret_key = SECRET_KEY
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16 MB upload limit

    # Init DB
    init_db()

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(train_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(sim_bp)
    app.register_blueprint(emergency_bp)

    # Inject app name into all templates
    @app.context_processor
    def inject_globals():
        return {"app_name": APP_NAME}

    return app


if __name__ == "__main__":
    app = create_app()
    print("Starting server at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
