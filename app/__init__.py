import logging
from flask import Flask
from app.config import Config
from app.models.users import User
from app.extensions import db, csrf
from app.models.weather import Weather


def create_app(config_class=Config):
    """
    Developer: Utsab Dutta
    Version: v1.1
    Description: "To create Flask App which will have login, registration, searching features"

    :param config_class: config files
    :return: app
    """
    # Initialize Flask app here
    app = Flask(__name__)
    # Initialize Logger  here
    logger = logging.getLogger(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        db.session.commit()
        logger.info("INFO: Database got Created")

    # Register blueprints here
    from app.main import login_bp, logout_bp, index_bp, dashboard_bp, register_bp, current_weather_bp, \
        history_weather_bp
    app.register_blueprint(login_bp)
    app.register_blueprint(logout_bp)
    app.register_blueprint(index_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(current_weather_bp)
    app.register_blueprint(history_weather_bp)
    logger.info("INFO: Blueprint Register for Sites")

    from app.apis import api_generate_token_bp, api_get_all_users_bp, api_history_weather_bp, api_current_weather_bp, \
        api_custom_weather_bp
    app.register_blueprint(api_generate_token_bp, url_prefix='/api')
    app.register_blueprint(api_get_all_users_bp, url_prefix='/api')
    app.register_blueprint(api_history_weather_bp, url_prefix='/api')
    app.register_blueprint(api_current_weather_bp, url_prefix='/api')
    app.register_blueprint(api_custom_weather_bp, url_prefix='/api')
    logger.info("INFO: Blueprint Register for APIs")

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8080, ssl_context=('./certificates/server.crt', './certificates/server.key'))
