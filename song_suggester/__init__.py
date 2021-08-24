'''entry-point for app'''

from .app import create_app
from dotenv import load_dotenv


load_dotenv('.flaskenv')
load_dotenv('.env')

APP = create_app()