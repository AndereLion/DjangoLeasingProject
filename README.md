# Car leasing application

This is a web application built using Python and Django that allows users to register and choose a car to purchase on
lease. The application also allows staff users to add and delete cars from the system.

### Installation and Setup

Clone the repository to your local machine

Ensure that you have Python and Django installed on your system

Create a virtual environment for the project
Install the required dependencies by running the following command:

`- pip install -r requirements.txt`

Run the migrations to create the database tables by running the following command:

`- python manage.py migrate`

Create a superuser to access the admin panel by running the following command and providing the required details:

`- python manage.py createsuperuser`

Run the development server by running the following command:

`- python manage.py runserver`

The application can be accessed by visiting `http://localhost:8000/` in your browser.

### Features

`User Registration and Login`

Users can register for an account on the application using a registration form. Once registered, users can log in to
their account using their username and password.

Car Selection and Lease Calculation
Registered users can select a car from a list of available cars and calculate the cost of leasing the car based on the
selected lease term, down payment, and interest rate.

Staff-Only Functionality
Staff users have access to additional functionality on the application. They can add new cars to the system and delete
existing cars.
