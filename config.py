import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://omid:Ordopor31OD@127.0.0.1/hendooneh'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


