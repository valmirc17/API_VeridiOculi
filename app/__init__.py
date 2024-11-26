from flask import Flask
from flask_pymongo import PyMongo
import logging

# Configuração do logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),  # Log no console
        logging.FileHandler("app.log"),  # Log em arquivo
    ]
)

logger = logging.getLogger(__name__)


mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb+srv://api_veridi:8BaFym9x6e8OIGsi@veridioculi.qqcq3.mongodb.net/veridi?retryWrites=true&w=majority&appName=VeridiOculi"
    app.config["SECRET_KEY"] = "API_VERIDI_SECRET"
    mongo.init_app(app)

    # Registrando os controladores nas rotas
    from app.controllers.userController import user_bp
    from app.controllers.analysisController import analysis_bp
    # from app.controllers.reportController import report_bp

    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(analysis_bp, url_prefix="/analysis")
    # app.register_blueprint(report_bp, url_prefix="/reports")

    with app.app_context():
        try:
            mongo.db.list_collection_names()
            logger.info("\033[32mConexão com MongoDB realizada com sucesso!\033[0m")

        except Exception as e:
            logger.error(f"\033[31mErro ao conectar com o banco de dados: {e}\033[0m")

    return app

    