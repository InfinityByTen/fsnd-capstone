import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
from dataclasses import dataclass
import json

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()


def setup_db(app, db_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


def db_drop_and_create_all():
    db.drop_all()
    db.create_all()
    init_db()


class BasicDbOps:
    ''' 
    This class is to handle the common basic db ops for each db.Model

    Attributes: 
        real (int): The real part of complex number. 
        imag (int): The imaginary part of complex number. 
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()


@dataclass
class Actor(db.Model, BasicDbOps):
    __tablename__ = 'Actors'

    id:  int
    name:  str
    age:  int
    gender:  str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)
    movie_ref = db.relationship('Movie', backref='actor', lazy=True)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


@dataclass
class Movie(db.Model, BasicDbOps):
    __tablename__ = "Movies"

    id:  int
    title:  str
    requirements:  json
    release_date:  datetime.date

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    requirements = db.Column(db.JSON, nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    selected_actor = db.Column(
        db.Integer, db.ForeignKey('Actors.id'), nullable=True)

    def __init__(self, title, requirements, release_date):
        self.title = title
        self.requirements = json.loads(requirements)
        self.release_date = release_date


def init_db():
    actors = [
        Actor(name="Tom Cruise", age=57, gender="M"),
        Actor(name="George Clooney", age=58, gender="M"),
        Actor(name="Mila Kunis", age=36, gender="F"),
        Actor(name="Gal Gadot", age=34, gender="F"),
        Actor(name="Halle Berry", age=57, gender="F")
    ]

    db.session.add_all(actors)

    movies = [
        Movie(title="Oceans 11",
              release_date=datetime.date(day=1, month=1, year=2021),
              requirements='{"age_min":25,"age_max":55,"gender":"M"}'),
        Movie(title="Wonder Women",
              release_date=datetime.date(day=1, month=1, year=2022),
              requirements='{"age_min":25,"age_max":55,"gender":"F"}'),
        Movie(title="Casino Royale",
              release_date=datetime.date(day=1, month=1, year=2023),
              requirements='{"age_min":25,"age_max":55,"gender":"F"}')
    ]

    db.session.add_all(movies)
    db.session.commit()
