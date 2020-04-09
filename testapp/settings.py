import os

SECRET_KEY = '123'

current_path = os.getcwd()
path_to_db = os.path.join(current_path, 'main.db')
SQLALCHEMY_DATABASE_URI = f'sqlite:///{path_to_db}'
