# journey-planner

### Notes on environmental variables

The only environmental variable to be set is APPLICATION_CONFIG, which is "development" by default. 

This variable is used to load in a JSON configuration file containing the Flask env variable FLASK_ENV and user made FLASK_CONFIG which is used by the application factory to select the correct application config depending on whether you want to run this is in development or production.

To run the application, we run the following in command line:

`./manage.py flask run`

