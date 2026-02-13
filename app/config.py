import os

class Config:    
    # Prioridad: Variable de entorno > Valor por defecto
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave-muy-secreta')
    DATABASE_URL = os.environ.get('DATABASE_URL')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_by_name = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig    
}