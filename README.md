# Assignment-UP
Web application which will lists menu for a given restaurant (Backend and Frontend). Frontend has only been implemented on the local machine.

# Access via Internet (Backend only)
* Sorted Items - http://swatishree.tech/show/1
* Default Selection - http://swatishree.tech/show
* Search - http://swatishree.tech/search/5?name=%27Shikanji%27
* Filter - http://swatishree.tech/filter?food_type=%27Veg%27


## How to run the application locally (Backend and Frontend)
* [Download from Github](#download-from-github)
* [Run sql script to load dummy data in db](#dummy-data-for-project)
* [Run Flask(at manage.py location)](#run-flask)
* [Run Django](#run-django)


## Requirements Implemented
* [Sorted Items](#sorted-items)
* [Default Selection](#default-selection)
* [Search](#search)
* [Filter](#filter)
* [Pagination](#pagination)


### Download from Github
* Download and extract the code from - https://github.com/swatishree26/assignment-UP/archive/master.zip
* Or Clone the repository - https://github.com/swatishree26/assignment-UP.git


### Dummy data for project
* Create database - "fooddetails" from dummy_data.sql on sql server
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


### Run Django
* pip install django
* pip3 install requests
* python3 manage.py runserver


### Sorted Items
* Items within each category are displayed in alphabetical order based on "name"
* url_path : http://127.0.0.1:8000/show/1
* url_path : http://swatishree.tech/show/1


### Default Selection
* Items from default category (first) are displayed
* url_path : http://127.0.0.1:8000
* url_path : http://swatishree.tech/show


### Search
* Items are searchable via backend. Could not implement for frontend
* url_path (searching for Shikanji under Beverages category) : http://127.0.0.1:5000/search/5?name=%27Shikanji%27
* url_path (searching for Shikanji under Beverages category): http://swatishree.tech/search/5?name=%27Shikanji%27


### Filter
* Veg Only option has been implemented
* url_path : http://127.0.0.1:5000/filter?food_type=%27Veg%27
* url_path : http://swatishree.tech/filter?food_type=%27Veg%27


### Pagination
* Not yet implemented

