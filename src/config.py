from dotenv import load_dotenv
import os

load_dotenv("/Users/voron/Desktop/shift/shift-rest/.env")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

if __name__ == '__main__':
    print(type(DB_PORT))