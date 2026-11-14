from dotenv import load_dotenv 
from os import getenv


load_dotenv()

DB_URL = getenv("DB_URL")
DB_USER = getenv("DB_USER")
DB_PWD = getenv("DB_PWD")


