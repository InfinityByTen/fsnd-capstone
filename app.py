import os
from dataclasses import asdict
from flask import Flask, request, abort, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
import re

from models import setup_db, MovieSchema, ActorSchema, Actor, Movie


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    setup_db(app)
    return app


APP = create_app()


# Model Schema validation helper
def formatted_json_validation_error(error):
    return jsonify({"success": False, "error": re.sub(
        " {4,}", " ", str(error).replace("\n", ' '))}), 422


# ROUTES
'''
    GET index
        just a simple health check
'''


@APP.route('/')
def health_check():
    return jsonify("Healthy")


'''
    GET /movies
        get all movies
        @TODO: add auth get:movies
'''


@APP.route('/movies')
def get_movies():
    try:
        movies = Movie.query.all()
        return jsonify({"success": True, "movies": movies})
    except Exception as e:
        print(e)
        abort(422)


'''
    GET /movies/id
        get specific movie by id
        @TODO: add auth get:movies
'''


@APP.route('/movies/<int:movie_id>')
def get_movie_by_id(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        abort(404)
    else:
        return jsonify({"success": True, "movies": movie})


'''
    POST /movies/new
        create a new movie entry
        @TODO: add auth post:movies
'''


@APP.route('/movies/new', methods=['POST'])
def add_new_movie():
    try:
        data = json.loads(request.data)
        print(data)
    except Exception as e:
        print(e)
        abort(400)
    try:
        entry = MovieSchema.from_dict(data)
        entry_dict = asdict(entry)
        movie = Movie(title=entry_dict['title'],
                      requirements=json.dumps(entry_dict['requirements']),
                      release_date=entry_dict['release_date'])
        print(movie)
        movie.insert()
        return jsonify({"success": True})
    except Exception as e:
        return formatted_json_validation_error(e)


'''
    PATCH /movies/id
        edit a movie entry with id
        @ TODO: add auth patch:movies
'''


@APP.route('/movies/<int:movie_id>', methods=['PATCH'])
def patch_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        abort(404)
    try:
        data = json.loads(request.data)
        print("Request to patch Movie #", movie_id)
        print(data)
        return jsonify({"success": True})
    except Exception as e:
        print(e)
        abort(422)


'''
    DELETE /movies/id
        delete a movie entry with id
        @TODO: add auth delete:movies
'''


@APP.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)
    if not movie:
        abort(404)
    try:
        print("Request to delete Movie #", movie_id)
        movie.delete()
        return jsonify({"success": True, "movie": movie})
    except Exception as e:
        print(e)
        abort(422)


'''
    GET /actors
        get all actors
        @TODO: add auth get:actors
'''


@APP.route('/actors')
def get_actors():
    try:
        actors = Actor.query.all()
        return jsonify({"success": True, "actors": actors})
    except Exception as e:
        print(e)
        abort(422)


'''
    GET /actors/id
        get specific actor by id
        @TODO: add auth get:actors
'''


@APP.route('/actors/<int:actor_id>')
def get_actor_by_id(actor_id):
    actor = Actor.query.get(actor_id)
    if not actor:
        abort(404)
    else:
        return jsonify({"success": True, "actors": actor})


'''
    POST /actors/new
        create a new actor entry
        @TODO: add auth post:actors
'''


@APP.route('/actors/new', methods=['POST'])
def add_new_actor():
    try:
        data = json.loads(request.data)
        print(data)
    except Exception as e:
        print(e)
        abort(400)
    try:
        entry = ActorSchema.from_dict(data)
        entry_dict = asdict(entry)
        actor = Actor(name=entry_dict['name'],
                      age=entry_dict['age'],
                      gender=entry_dict['gender'])
        print(actor)
        actor.insert()
        return jsonify({"success": True})
    except Exception as e:
        return formatted_json_validation_error(e)


'''
    PATCH /actors/id
        edit an actor entry with id
        @TODO: add auth patch:actors
'''


@APP.route('/actors/<int:actor_id>', methods=['PATCH'])
def patch_actor(actor_id):
    actor = Actor.query.get(actor_id)
    if not actor:
        abort(404)
    try:
        data = json.loads(request.data)
        print("Request to patch Actor #", actor_id)
        print(data)
        return jsonify({"success": True})
    except Exception as e:
        print(e)
        abort(422)


'''
    DELETE /actors/id
        delete an actor entry with id
        @TODO: add auth delete:actors
'''


@APP.route('/actors/<int:actor_id>', methods=['DELETE'])
def delete_actor(actor_id):
    actor = Actor.query.get(actor_id)
    if not actor:
        abort(404)
    try:
        print("Request to delete Actor #", actor_id)
        actor.delete()
        return jsonify({"success": True, "actor": actor})
    except Exception as e:
        abort(422)


# Error Handling

@APP.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


'''
    Error handler for 404
'''


@APP.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not Found"
    }), 404


'''
    Error handler for 500
'''


@APP.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Your request was not a correct json"
    }), 400


'''
    Error handler for AuthError
'''


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
