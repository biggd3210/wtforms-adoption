"""Models for adoption app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """connects app from app.py to database."""

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet Model"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    name = db.Column(db.Text,
                     nullable=False)
    
    species = db.Column(db.Text,
                        nullable=False)
    
    photo_url = db.Column(db.Text,
                          nullable=True,
                          default="https://media.istockphoto.com/id/541833910/vector/dog-and-cat-icon.jpg?s=612x612&w=0&k=20&c=n8AwpvJKqLKiHXDQUMeIN_PohTMxLFZ-LvlHg-PDgmc=")

    age = db.Column(db.Integer,
                    nullable=True)

    notes = db.Column(db.Text,
                      nullable=True)

    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)    