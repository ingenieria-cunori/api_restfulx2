from flask import Flask
from .config import config_by_name
from .api.namespaces import api
import os

def create_app(config_name=None):
    
    if not config_name:
        config_name = os.environ.get('FLASK_ENV', 'dev')

    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])    
    
    api.init_app(app)
    
    print("***********************")
    print(f"ENTORNO: {config_name}")
    print(f"SECRET_KEY: {app.config['SECRET_KEY']}")
    print("***********************")
    
    return app