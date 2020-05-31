import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True #웹서버에서 내용 자동 반영시킴
    MAIL_SUBJECT_PREFIX = '[goblin]'
    MAIL_SENDER = 'Goblins Admin<monster2z.mars@gmail.com>'
    FLASK_ADMIN=os.environ.get('FLASK_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER= 'smtp.googlemail.com'
    MAIL_PORT= 587
    MAIL_USE_TLS= True
    MAIL_USERNAME= os.environ.get('MAIL_USERNAME') #admin으로 함께 사용
    MAIL_PASSWORD= os.environ.get('MAIL_PASSWORD')      

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config): 
    DEBUG=True
    SQLALCHEMY_DATABASE_URI= os.environ.get('DEV_DATABASE_URL')            

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

config={
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'Production':ProductionConfig,
    'default' : DevelopmentConfig
}
