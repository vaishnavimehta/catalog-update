import sys
import os
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Catalog(Base):
	__tablename__ = 'catalog'
	id = Column(Integer,primary_key=True)
	image = Column(String(200), unique=True)

engine = create_engine('sqlite:///restaurantmenuwithusers.db')
Base.metadata.create_all(engine)
