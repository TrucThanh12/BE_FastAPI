from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('mysql+pymysql://root:trucdien1812@localhost/pizza_fastapi')

Base = declarative_base()

Session = sessionmaker()