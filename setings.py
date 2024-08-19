import os

from dotenv import load_dotenv


load_dotenv()

HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
