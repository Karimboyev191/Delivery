from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("postgresql://postgres:19601961@localhost/delivery_db")

Base = declarative_base()
session = sessionmaker()
