from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
import mongoengine
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config.from_object('config')
db = None#SQLAlchemy(app)
CORS(app)

mongoengine.connect('aftsabgardun')

from app import views, models


