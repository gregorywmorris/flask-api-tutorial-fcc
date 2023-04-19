from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    content= db.Column(db.String(200), nullable=False)
    completed= db.Column(db.Integer, default=0)
    date_created= db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id
    # code used once to create intial database
    with app.app_context():
        db.create_all()