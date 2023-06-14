import os

import dotenv

dotenv.load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_HOST = os.getenv('POSTRGES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

MIN_STUDENT_AGE = 17
MIN_TEACHER_AGE = 22
