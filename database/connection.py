from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db = create_engine('mysql+pymysql://root:mysql123@localhost/sistema_pizzaria')

Session = sessionmaker(bind=db)

Base = declarative_base()

