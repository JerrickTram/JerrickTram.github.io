import os

# Retrieve environment variables or use default values if not set
SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False
