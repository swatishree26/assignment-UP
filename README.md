# Assignment-UP
Web application which will lists the menu for a given restaurant (Backend and Frontend)

## How to run the application locally
* [Download from Github](#download)
* [Run sql script to load dummy data in db](#sqldata)
* [Run Flask](#flask)
* [Run Django](#django)

## Requirements Implemented
* [Sorted Items](#sorted)
* [Default Selection](#default)
* [Search](#search)
* [Filter](#filter)
* [Pagination](#pagination)

### Download from Github
* Download and extract the code from - https://github.com/swatishree26/assignment-UP/archive/master.zip
* Or Clone the repository - https://github.com/swatishree26/assignment-UP.git

### Dummy data for project
* Create database - "fooddetails"
* Complete all the steps under run flask
* Run the sql script(dummy_data.sql) on sql server
* Edit sql pass credentials in config.py (/instance)

### Run Flask
* pip install Flask
* pip install flask_sqlalchemy
* pip install flask_mysqldb
* pip install flask_migrate
* export FLASK_ENV=development
* export FLASK_APP=server.py
* flask db init
* flask db upgrade
* flask db migrate
* flask run

### Run Django (at manage.py location)
* python3 manage.py runserver

### Sorted Items
* Items within each category are displayed in alphabetical order based on "name"
* url_path : http://127.0.0.1:8000/show/1/

### Default Selection
* Items from default category (first) are displayed
* url_path : http://127.0.0.1:8000

### Search
* Items are searchable via backend. Could not implement for frontend
* url_path : http://127.0.0.1:5000/search/5?name='Shikanji'

### Filter
* Veg Only option has been implemented
* url_path : http://127.0.0.1:5000/filter?food_type='Veg'

### Pagination
* Not yet implemented

