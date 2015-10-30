import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
DATABASE_HOST = 'localhost'
DATABASE_USERNAME = 'root'
DATABASE_NAME = 'foodcon'
DATABASE_PASSWORD = ''
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_TRACKABLE = True
SECURITY_PASSWORD_SALT = 'foodcon_super_password'
