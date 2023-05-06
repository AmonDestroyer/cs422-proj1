## Description

## Authors
Adam Case, Brett Fox, Josh Sawyer, Luke Scribner, and Sophia Zhang

## Creation Date

## CS422 Project1

## Software Dependencies
Required Software:
* Python 3.8
* pip

Required Packages:
* pipenv
* django
* mysqlclient
* scikit-learn
* pytz
* tzdata

## .env File
You will need to create a file named ".env" in the root directory of the project to be able to run the app locally. The file's content should look like this: \
`SECRET_KEY=93dd754550f9bc00d62576012a920193b88d22a536303c19` \
`DB_NAME=422` \
`USER=dev` \
`PASSWORD=hurricane422` \
`HOST=ix.cs.uoregon.edu` \
`PORT=3070`




## Steps to run locally
* Install [python](https://www.python.org/), verify pip is installed using the command: \
 `python -m ensurepip --upgrade` \
 If pip is not installed, see [here](https://pip.pypa.io/en/stable/installation/)

* Clone this repository to your local machine
* Create .env file in root dir (see above)
* cd to 422-proj1/Backend
* Run: `pip install pipenv`
* Run: `pipenv install --dev`
* Run: `pipenv shell\`
* Run: `python manage.py runserver`
* Navigate to 127.0.0.1:8000 in web browser


## Directory structure
### TSProject
Contains the Django project settings (settings.py) and url.py file that routes incoming urls to their appropriate app. It also contains all the static files (in the static folder) and Django uses this folder to serve them when the an html template requests (icons, css, js).

### roles
The app responsible for login functionality. Renders the login page to the frontend, but is able to be scaled to include authentication. It contains urls.py and views.py where urls.py directs the url request to views.py where views.py handles the request and responds back to the frontend. It also containes a template folder to hold the templates to be rendered to the frontend. 

### time_series
The app responsibile for loading all pages (apart from the login page) and accessing the database. This contains views.py and urls.py (same functionality as roles). A template folder is present to hold all the html templates to be rendered to the frontend. It also contains three main modules: calculate, download, and upload. Calculate gets the mean squared error of the uploaded solution. Download is responsible for pulling the requested information from the database. Upload is responsible for pushing information (TS Sets and their meta data) to the database.
