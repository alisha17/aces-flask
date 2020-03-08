import os

# Statement for enabling the development environment
DEBUG = True

# Define the application directory

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True

DATABASE_NAME = "aces"
DATABASE_HOST = "localhost"
DATABASE_PORT = 27017

SECRET_KEY = "okay"
JWT_SECRET_KEY = "jwt-secret-string"

CORS_HEADERS = "Content-Type"
