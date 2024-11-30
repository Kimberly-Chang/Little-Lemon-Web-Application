# Little-Lemon-Web-Application
This project is a Django web app for the Meta Back-End Developer Capstone course. 

## Sample API Calls
Some sample API calls are provided in the [sample_API_calls.json](sample_API_calls.json) file. This file can be imported into [Insomnia](https://insomnia.rest/).

## Notable API Endpoints
### /auth/token/login/
This is an authentication endpoint for user login. This endpoint returns a token if the provided login credentials are valid. This is an endpoint automatically generated by Djoser.

### /auth/token/logout/
This is an authentication endpoint for user logout. The endpoint will return a 204 response upon successful logout. This is an endpoint automatically generated by Djoser.

### /restaurant/booking/tables/
This endpoint **requires authorization**. The user must be logged in to access this endpoint. There is currently no difference in types of users.

This endpoint allows the user to view and edit bookings.

### /restaurant/menu/
This endpoint allows the user to view and create menu items. This endpoint displays all menu items in a paginated format.

### /restaurant/menu/1
This endpoint allows the user to edit or delete specific menu items. This example uses `1`, but any number corresponding to the `id` of a `Menu` item can be used.

### /restaurant/ 
This is not an API endpoint, but it is a webpage from a provided HTML template with provided static elements.


## Running the Project
### Dependencies
This project uses a MySQL database, so the MySQL server must be installed. You can download it [here](https://dev.mysql.com/downloads/installer/).

This project uses `pipenv` for its virtual environment. If `pipenv` is not yet installed, please install it using `pip install pipenv`. 

This project was made with Python 3.12, but it may be possible to run this project with other versions of Python 3. If you are using a different Python 3, you can change the Python 3.12 requirement in the Pipfile to Python 3. 

Install project dependencies using `pipenv install`.

Adjust the `DATABASES` in [settings.py](littlelemon/littlelemon/settings.py) as needed for your database. Then, use `python manage.py migrate` while in the [littlelemon](littlelemon/) folder to update the database to be used for this project. 

The project can then be run with `python manage.py runserver` while in the [littlelemon](littlelemon/) folder.
