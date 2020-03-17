import os
from dotenv import load_dotenv
load_dotenv()

ES_CLIENT_URL = os.getenv("ES_CLIENT_URL")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

# print(ES_CLIENT_URL)
# print(DB_HOST, DB_USER, DB_PASS, DB_NAME)