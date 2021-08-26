from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_restful import Api
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.environ['user']}:{os.environ['password']}@{os.environ['host']}/{os.environ['database']}"
api = Api(app)
db = SQLAlchemy(app)

from web_count.views import WebsiteView

api.add_resource(WebsiteView, 
	'/website',
	'/website/<int:pk>'
	)