## Description

## Authors
Adam Case, Brett Fox, Josh Sawyer, Luke Scribner, and Sophia Zhang

## Creation Date

## CS422 Project1

## Steps to run locally

## Software Dependencies

## Directory structure
### TSProject
Contains the Django project settings (settings.py) and url.py file that routes incoming urls to their appropriate app. It also contains all the static files (in the static folder) and Django uses this folder to serve them when the an html template requests (icons, css, js).

### roles
The app responsible for login functionality. Renders the login page to the frontend, but is able to be scaled to include authentication. It contains urls.py and views.py where urls.py directs the url request to views.py where views.py handles the request and responds back to the frontend. It also containes a template folder to hold the templates to be rendered to the frontend. 

### time_series
The app responsibile for loading all pages (apart from the login page) and accessing the database. This contains views.py and urls.py (same functionality as roles). A template folder is present to hold all the html templates to be rendered to the frontend. It also contains three main modules: calculate, download, and upload. Calculate gets the mean squared error of the uploaded solution. Download is responsible for pulling the requested information from the database. Upload is responsible for pushing information (TS Sets and their meta data) to the database.
