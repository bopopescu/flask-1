class Configuration(object):
    DEBUG = True
    sqlalchemy_track_modifications=False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1234@localhost/test1'