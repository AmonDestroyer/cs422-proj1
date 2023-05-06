# CS422 Project1
This project is part of the University of Oregon's CS 422 (Software Methodologies) Course taken by thea authros during Spring 2023.

## Description
This repository contains the back-end and front-end for a web application dealing with developement of timeseries storage web application. Additional steps will need to be taken to install and create a MySQL database to connect to this applicaiton once built.

## Authors
Adam Case, Brett Fox, Josh Sawyer, Luke Scribner, and Sophia Zhang

## Creation Date
* 4/6/23: Project Development Began
* 5/5/23: Project Development Completed

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
You will need to create a file named ".env" in the /Backend/ directory of the project to be able to run the app locally. The file's content should look like this: \
`SECRET_KEY=93dd754550f9bc00d62576012a920193b88d22a536303c19` \
`DB_NAME=422` \
`USER=dev` \
`PASSWORD=hurricane422` \
`HOST=ix.cs.uoregon.edu` \
`PORT=3070`


## Steps to run locally on Windows
####  Steps for running on other OS's are similar, but minor modifications may need to be made, such as replacing 'python' with 'python3' when running commands. If you're experiencing database-related issues, try replacing the database variables in /Backend/TSProject/settings.py such as `'USER': os.environ['USER'],` with the raw values from the .env file.

* Install [python](https://www.python.org/), verify pip is installed using the command: \
 `python -m ensurepip --upgrade` \
 If pip is not installed, see [here](https://pip.pypa.io/en/stable/installation/)

* Clone this repository to your local machine
* Create .env file in /Backend/ dir (see above)
* cd to 422-proj1/Backend
* Run: `pip install pipenv`
* Run: `pipenv install --dev`
* Run: `pipenv shell`
* Run: `python manage.py runserver`
* Navigate to 127.0.0.1:8000 in web browser

## Setting up local mysql server
* Install mysql for your OS and set up a user with full permissions by following the [documentation](https://dev.mysql.com/doc/mysql-getting-started/en/#mysql-getting-started-installing)
* Once the mysql server is running, run the `proj1_db_generator_v3.sql` script to generate the correct schema and tables
* Finally, replace the values in the .env file with your new local database information


## Directory structure
### TSProject
Contains the Django project settings (settings.py) and url.py file that routes incoming urls to their appropriate app. It also contains all the static files (in the static folder) and Django uses this folder to serve them when the an html template requests (icons, css, js).

### roles
The app responsible for login functionality. Renders the login page to the frontend, but is able to be scaled to include authentication. It contains urls.py and views.py where urls.py directs the url request to views.py where views.py handles the request and responds back to the frontend. It also containes a template folder to hold the templates to be rendered to the frontend. 

### time_series
The app responsibile for loading all pages (apart from the login page) and accessing the database. This contains views.py and urls.py (same functionality as roles). A template folder is present to hold all the html templates to be rendered to the frontend. It also contains three main modules: calculate, download, and upload. Calculate gets the mean squared error of the uploaded solution. Download is responsible for pulling the requested information from the database. Upload is responsible for pushing information (TS Sets and their meta data) to the database.
