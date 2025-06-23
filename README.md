#### Late Night Show API

This Flask application provides a backend API for managing guests, episodes, and appearances on a late night talk show. It includes user authentication and authorization features to protect sensitive operations.

### Features

User Authentication: Secure registration and login with JWT tokens

Guest Management: List all guests with their occupations

Episode Management: List all episodes

View episode details with appearances

Delete episodes (admin only)

Appearance Management: Create new guest appearances (authenticated users only)

Rate appearances (1-5 scale)

Database Relationships:

Guests appear in episodes

Episodes have multiple appearances

Users can register and login

Technologies Used
Backend: Python, Flask

Database: PostgreSQL

ORM: SQLAlchemy

Authentication: Flask-JWT-Extended

Database Migrations: Flask-Migrate

API Testing: Postman

### Setup and Installation
## Prerequisites

Python 3.8+

PostgreSQL

Pipenv (recommended) or pip

### Installation Steps
Clone the repository:

git clone https://github.com/yourusername/late-night-show-api.git
cd late-night-show-api

Set up virtual environment:

pipenv install && pipenv shell
## Install dependencies:

pip install -r requirements.txt
Create .env file:
DATABASE_URL=postgresql://username:password@localhost/late-night-show
SECRET_KEY=your-flask-secret-key
JWT_SECRET_KEY=your-jwt-secret-key
Set up database:

flask db upgrade
python seed.py
Running the Application

#### export FLASK_APP=server.app 

flask run --port=5555
The API will be available at http://localhost:5555

### Testing with Postman
Import the Postman collection

Set environment variables:

base_url: http://localhost:5555

Test workflow:

Register a new user

Login to get access token

Use token to access protected endpoints

