import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Actor, Movie

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  CORS(app)
  setup_db(app)
  return app

APP = create_app()

@APP.route('/')
def health_check():
    return jsonify("Healthy")

@APP.route('/db')
def db_status():
    actor_count = Actor.query.count()
    movie_count = Movie.query.count()
    return jsonify({"actors":actor_count, "movies":movie_count})

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)