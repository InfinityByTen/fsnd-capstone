# Casting Agency App

## Introduction

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. It provides an `API` to interact with their database providing `CRUD` for actors and movies, depending on the permissions of the user. The permissions in this project are created and managed on [Auth0](https://auth0.com). The project includes configuration files to deploy it on [Heroku](https://heroku.com).

## Getting Started

This repo has the backend in the root of the directory. The main application is in `app.py`. The `Procfile`, `setup.sh` and `requirements.txt` are to deploy the app on `Heroku` and hence in the root.

To ensure you have all the requirements, install them locally or in a virtual environment:

```bash
pip3 install -r requirements.txt
```

The app relies on a `postgres` database, which can be created locally with

```bash
createdb <chose_any_name>
```

Add the name of the db as an environment variable `DATABASE_URL` like so:
```bash
export DATABASE_URL=<db_name>
```
To initialize the database with some dummy values, you can invoke the `release_new.py`. You can then initiate the app directly via `flask` with

```bash
export FLASK_APP=app.py
export FLAS_ENV=production
flask run
```
or simply with `python`

```bash
python3 app.py
```
or start with a `WSGI` server

```bash
gunicorn app:APP
```
The `Heroku` deployment runs the `gunicorn` version.


## Tests

Tests are a standalone portion of the project. There are two sets of test suites: unit tests for checking the app functionality and a postman collection to test the `RBAC` logic. 

Once you have a local app running, you can read more about the tests in [.tests](.test/README.md).


## Frontend

A frontend to get `JWT` tokens is added as a sub-directory. The frontend is also a standalone folder and contains all the relevant information on how to get started and use. It's main purpose is only to get valid `JWT` to test the endpoint locally or the one hosted on `Heroku`.

You can read more about it in [.frontend](.frontend/README.md).


## API Reference

### Endpoints

* MOVIES
    <details>
    <summary>GET</summary>

    1. All movies
    * `GET /movies`
    * Sample Response [json]
        ```yaml
            {
                "success": True,
                "movies": [
                    {
                        "id": 1,
                        "release_date": "Fri, 01 Jan 2021 00:00:00 GMT",
                        "requirements": {
                            "age_max": 55,
                            "age_min": 25,
                            "gender": "M"
                        },
                        "title": "Movie 1"
                    },
                    {
                        "id": 2,
                        "release_date": "Sat, 01 Jan 2022 00:00:00 GMT",
                        "requirements": {
                            "age_max": 55,
                            "age_min": 25,
                            "gender": "F"
                        },
                        "title": "Movie 2"
                    }
            }
        ```

    2. Specific movie by id
    * `GET - /movies/movie_id`
    * Request Parameters movie_id=[integer]
    * Sample Response [json]
            ```yaml
                {
                    "success": True,
                    "movies": {
                        "id": 1,
                        "release_date": "Fri, 01 Jan 2021 00:00:00 GMT",
                        "requirements": {
                            "age_max": 55,
                            "age_min": 25,
                            "gender": "M"
                        },
                        "title": "Movie 1"
                    }
                }
            ```
    </details>

    <details>
    <summary>POST</summary>

    * `POST /movies/new`
    * Sample Body [json]
            ```yaml
            {
                "title":"Movie Title",
                "release_date":"12-12-12",
                "requirements":{"age_min":20, "age_max":40, "gender":"M"}
            }
            ```
    * Sample Response [json]
            ```yaml
             {
                 "success": True
             }
            ```
    </details>

    <details>
    <summary>PATCH</summary>

    * `PATCH /movies/movie_id`
    * Request Parameters - movie_id=[integer]
    * Sample Body [json]
            ```yaml
            {
                "release_date":"12-12-12",
                "requirements":{"age_min":20, "age_max":50, "gender":"M"}
            }
            ``` 
    * Sample Response [json]
            ```yaml
             {
                 "success": True,
                 "movie": {
                        "id": 1,
                        "release_date": "Wed, 12 Dec 2012 00:00:00 GMT",
                        "requirements": {
                            "age_max": 55,
                            "age_min": 25,
                            "gender": "M"
                        },
                        "title": "Movie 1"
                }
             }
            ```
    </details>

    <details>
    <summary>DELETE</summary>

    * `DELETE  /movies/movie_id`
    * Request Parameters - movie_id=[integer]
    * Sample Response [json]
            ```yaml
             {
                 "success": True,
                 "movie": {
                        "id": 1,
                        "release_date": "Wed, 12 Dec 2012 00:00:00 GMT",
                        "requirements": {
                            "age_max": 55,
                            "age_min": 25,
                            "gender": "M"
                        },
                        "title": "Movie 1"
                }
             }
            ```
    </details>

* ACTORS
    <details>
    <summary>GET</summary>

    1. All actors
    * `GET - /actors`
    * Sample Response [json]
            ```yaml
             {
                 "success": True,
                 "actors": [
                    {
                        "age": 57,
                        "gender": "M",
                        "id": 1,
                        "name": "Tom Cruise"
                    },
                    {
                        "age": 58,
                        "gender": "M",
                        "id": 2,
                        "name": "George Clooney"
                    }
             }
            ```

    2. Specific actor by id
    * `GET  /actors/actor_id`
    * Request Parameters - actor_id=[integer]
    * Sample Response [json]
            ```yaml
             {
                "actors": {
                    "age": 57,
                    "gender": "M",
                    "id": 1,
                    "name": "Tom Cruise"
                },
                "success": true
             }
            ```
    </details>

    <details>
    <summary>POST</summary>

    * `POST /actors/new`
    * Sample Body [json]
            ```yaml
                {
                    "name":"Popat Lal",
                    "age":38,
                    "gender":"M"
                }
            ```
    * Sample Response [json]
            ```yaml
             {
                 "success": True
             }
            ```
    </details>

    <details>
    <summary>PATCH</summary>

    * `PATCH /actors/actor_id`
    * Request Parameters - actor_id=[integer]
    * Sample Body [json]
            ```yaml
                {
                    "name":"Anonymous"
                    "gender":"F"
                }
            ```
    * Sample Response [json]
            ```yaml
                {
                    "actors": {
                        "age": 57,
                        "gender": "F",
                        "id": 1,
                        "name": "Anonymous"
                    },
                    "success": true
                }
            ```
    </details>

    <details>
    <summary>DELETE</summary>

    * `DELETE /actors/actor_id`
    * Request Parameters - actor_id=[integer]
    * Sample Response [json]
            ```yaml
             {
                "actors": {
                    "age": 57,
                    "gender": "M",
                    "id": 1,
                    "name": "Tom Cruise"
                },
                "success": true
             }
            ```
    </details>

### Errors

<details>
<summary>Unprocessable Entity</summary>

If your body doesn't meet the schema expectations you will get a `422` error with a message telling where you have made an error.

Response
```yaml
{
    "error": 422,
    "message": "'name' is a required property  Failed validating 'required' in schema: {'$schema': 'http://json-schema.org/draft-06/schema#', 'description': 'Actor Format', 'properties': {'age': {'type': 'integer'}, 'gender': {'type': 'string'}, 'name': {'type': 'string'}}, 'required': ['name', 'age', 'gender'], 'type': 'object'}  On instance: {'age': 38, 'gender': 'M', 'naame': 'New Hunk'}",
    "success": false
}
```
</details>

<details>
<summary>Not Found</summary>

If you try to access a resource that is not available, you get a `404` error.

Response
```yaml
{
    "error": 404,
    "message": "Not Found",
    "success": false
}
```

</details>

<details>
<summary>Bad Request</summary>

If your request body is not a well formed `json`, you will get a `400` error.

Response
```yaml
{
    "error": 400,
    "message": "Your request was not a correct json",
    "success": false
}
```

</details>

<details>
<summary>Authorization Error</summary>

If your authorization credentals (`jwt`) is not corect, you will get `401` with a code and description giving more information what sort of authentication failed.

Response
```yaml
{
    "error": 401,
    "message": {
        "code": "error_code",
        "description": "Reason."
    },
    "success": false
}
```
</details>
