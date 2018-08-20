# Configurations for the app file


# The configurations fot the base class
class Config():
    DEBUG = True


# Defines the development environment variables
class DevelopmentConfig(Config):
    DEBUG = True


# Define the testing environment variables
class TestingConfig(Config):
    TESTING = True
    DEBUG = True


# Define production environment configurations
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


APP_CONFIG = {'development': DevelopmentConfig,
              'testing': TestingConfig,
              'production': ProductionConfig}
