import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DATABASE_URI = os.environ.get("DATABASE_URI")
TOKEN_SECRET_KEY = os.environ.get("TOKEN_SECRET_KEY")