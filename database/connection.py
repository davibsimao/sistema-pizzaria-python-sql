from os import getenv

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


load_dotenv()

DB_USER = getenv('DB_USER')
DB_PASSWORD = getenv('DB_PASSWORD')
DB_HOST = getenv('DB_HOST')
DB_NAME = getenv('DB_NAME')

DATABASE_URL = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

db = create_engine(DATABASE_URL)

Session = sessionmaker(bind=db)

Base = declarative_base()
