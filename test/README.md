# Testing

There are two sets of test suites for this project. The `RBAC` logic is tested via a postman collection. A sample run is also added for reference. It can be tested against both: a local server or the Heroku deployment. The unit tests are tested using `pytest`. They run with a admin or glabal jwt, which has all the access, so no `RBAC` logic should be involved. 

`admin_tokener.py` is added to get a `JWT` with these special permissions. You do not need to invoke it separately. It is taken care of by the test suite itself 

## Postman Collection

The postman collection is exported as a `.json` and a recent sample run has also been added. The `jwt`s needed for the different roles are just updated before upl;oading the changes and should last good for `24` hours from then. If not, feel free to create new using the frontend, provided you have the needed credentials shared to you.

|  WARNING: If you run the postman collection against the Heroku deployment, you might not be able to run it again, since it relies on a default state of the database (it also includes `DELETE` tests). If you try to delete the same resource twice, you will get a `404` and not a `200` or `401` depending on the permissions. |
|---|

## Unitests

Before running the tests, please ensure that the db is started up from scratch. Run from the root

```bash
   python3 release_new.py
```

Then `cd test`  and ensure the `test_app.py` has a correct `DATABASE_URL`. The tests need to be updated with the path of the database you created to run the app. Currenly it's a random location. Literally :)

Once that is ensured, you can run the test with 

```bash
   pytest test_app.py
```

If you did installed the requirements previously, then you should have all the modules needed to run the test. Else you can start a virtual environment from within the folder using the copy of `requirements.txt` which is provided in this folder.