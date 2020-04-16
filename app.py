import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json

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
    return jsonify({"actors": actor_count, "movies": movie_count})

# ROUTES


'''
    GET /movies
        get all movies
'''


@APP.route('/movies')
def get_movies():
    movies = Movie.query.all()
    return jsonify({"success": True, "movies": movies})


'''
    GET /movies/id
        get specific movie by id
'''


@APP.route('/movies/<int:movie_id>')
def get_movie_by_id(movie_id):
    movies = Movie.query.get(movie_id)
    return jsonify({"success": True, "movies": movies})


'''
    POST /movies/new
        create a new movie entry
'''


@APP.route('/movies/new', methods=['POST'])
def add_new_movie():
    data = json.loads(request.data)
    print(data)
    return jsonify({"success": True})


'''
    PATCH /movies/id
        edit a movie entry with id
'''


@APP.route('/movies/<int:movie_id>', methods=['PATCH'])
def patch_movie(movie_id):
    data = json.loads(request.data)
    print("Request to patch Movie #", movie_id)
    print(data)
    return jsonify({"success": True})


'''
    DELETE /movies/id
        delete a movie entry with id
'''


@APP.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    print("Request to delete Movie #", movie_id)
    return jsonify({"success": True})


'''
    GET /actors
        get all actors
'''


@APP.route('/actors')
def get_actors():
    actors = Actor.query.all()
    return jsonify({"success": True, "actors": actors})


'''
    GET /actors/id
        get specific actor by id
'''


@APP.route('/actors/<int:actor_id>')
def get_actor_by_id(actor_id):
    actors = Actor.query.get(actor_id)
    return jsonify({"success": True, "actors": actors})


'''
    POST /actors/new
        create a new actor entry
'''


@APP.route('/actors/new', methods=['POST'])
def add_new_actor():
    data = json.loads(request.data)
    print(data)
    return jsonify({"success": True})


'''
    PATCH /actors/id
        edit an actor entry with id
'''


@APP.route('/actors/<int:actor_id>', methods=['PATCH'])
def patch_actor(actor_id):
    data = json.loads(request.data)
    print("Request to patch Actor #", actor_id)
    print(data)
    return jsonify({"success": True})


'''
    DELETE /actors/id
        delete an actor entry with id
'''


@APP.route('/actors/<int:actor_id>', methods=['DELETE'])
def delete_actor(actor_id):
    print("Request to delete Actor #", actor_id)
    return jsonify({"success": True})


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
