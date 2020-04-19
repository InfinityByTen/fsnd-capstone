'''
Tests for fsnd capstone project.
'''

import os
import json
import pytest

import app
import models


@pytest.fixture
def client():
    # @TODO make the db configurable from the outside.
    os.environ['DATABASE_URL'] = "postgresql:///random"
    app.APP.config['TESTING'] = True
    client = app.APP.test_client()

    yield client


# Basic Health


def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == "Healthy"


# movies:get


def test_get_movies(client):
    response = client.get('/movies')
    assert response.status_code == 200
    assert len(response.json['movies']) == 3


def test_get_specific_movie(client):
    movie_id = 2
    response = client.get('/movies/'+str(movie_id))
    assert response.status_code == 200


def test_get_specific_movie_with_invalid_id_returns_not_found(client):
    movie_id = 1000
    response = client.get('/movies/'+str(movie_id))
    assert response.status_code == 404


# movies:post


def test_post_new_movie(client):
    body = {"title": "random", "release_date": "12-12-12",
            "requirements": {"age_min": 20, "age_max": 50, "gender": "M"}}
    response = client.post('/movies/new', data=json.dumps(body))
    assert response.status_code == 200


def test_post_new_movie_with_invalid_body(client):
    body = {"release_date": "12-12-12",
            "requirements": {"age_min": 20, "age_max": 50, "gender": "M"}}
    response = client.post('/movies/new', data=json.dumps(body))
    assert response.status_code == 422
    error_message = response.json['error']
    assert error_message is not None
    assert "'title' is a required property" in error_message


# movies:patch


def test_patch_movie(client):
    movie_id = 1
    body = {"title": "random", "date": "12-12-12",
            "requirements": {"age_min": 20, "age_max": 50, "gender": "M"}}
    response = client.patch('/movies/' + str(movie_id), data=json.dumps(body))
    assert response.status_code == 200


def test_patch_movie_with_invalid_body(client):
    movie_id = 1
    body = {"date": "12-12-12",
            "requirements": {"age_min": 20, "age_max": 50, "gender": "M"}}
    response = client.patch('/movies/' + str(movie_id), data=json.dumps(body))
    # @TODO: This should be failing with a malformed request or invalid params
    assert response.status_code == 200


def test_patch_movie_with_invalid_id(client):
    movie_id = 1000
    body = {"title": "random", "date": "12-12-12",
            "requirements": {"age_min": 20, "age_max": 50, "gender": "M"}}
    response = client.patch('/movies/' + str(movie_id), data=json.dumps(body))
    assert response.status_code == 404


    # movies:delete


def test_delete_specific_movie(client):
    movie_id = 2
    response = client.delete('/movies/'+str(movie_id))
    assert response.status_code == 200


def test_delete_specific_movie_with_invalid_id_returns_not_found(client):
    movie_id = 1000
    response = client.delete('/movies/'+str(movie_id))
    assert response.status_code == 404


# actors:get


def test_get_actors(client):
    response = client.get('/actors')
    assert response.status_code == 200
    assert len(response.json['actors']) == 5


def test_get_specific_actor(client):
    actor_id = 2
    response = client.get('/actors/'+str(actor_id))
    assert response.status_code == 200


def test_get_specific_actor_with_invalid_id_returns_not_found(client):
    actor_id = 10000
    response = client.get('/actors/'+str(actor_id))
    assert response.status_code == 404


# actors:post


def test_post_new_actor(client):
    body = {"name": "anonymous", "age": 42, "gender": "others"}
    response = client.post('/actors/new', data=json.dumps(body))
    assert response.status_code == 200


def test_post_new_actor_with_invalid_body(client):
    body = {"name": "anonymous", "gender": "others"}
    response = client.post('/actors/new', data=json.dumps(body))
    assert response.status_code == 422
    error_message = response.json['error']
    assert error_message is not None
    assert "'age' is a required property" in error_message


# actors:patch


def test_patch_actor(client):
    actor_id = 2
    body = {"name": "anonymous", "age": 42, "gender": "others"}
    response = client.patch('/actors/'+str(actor_id), data=json.dumps(body))
    assert response.status_code == 200


def test_patch_actor_with_invalid_body(client):
    actor_id = 2
    body = {"name": "anonymous", "gender": "others"}
    response = client.patch('/actors/'+str(actor_id), data=json.dumps(body))
    # @TODO: This should be failing with a malformed request or invalid params
    assert response.status_code == 200


def test_patch_actor_with_invalid_id(client):
    actor_id = 1000
    body = {"name": "anonymous", "age": 42, "gender": "others"}
    response = client.patch('/actors/'+str(actor_id), data=json.dumps(body))
    assert response.status_code == 404


# actors:delete


def test_delete_specific_actor(client):
    actor_id = 2
    response = client.delete('/actors/'+str(actor_id))
    assert response.status_code == 200


def test_delete_specific_actor_with_invalid_id_returns_not_found(client):
    actor_id = 10000
    response = client.delete('/actors/'+str(actor_id))
    assert response.status_code == 404
