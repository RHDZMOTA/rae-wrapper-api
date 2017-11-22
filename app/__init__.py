from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('app_config')

db = SQLAlchemy(app)


from app.mod_dictionary.controller import mod_dictionary as dictionary
app.register_blueprint(dictionary)


db.create_all()