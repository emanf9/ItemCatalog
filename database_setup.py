import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
    	return{
    	'id': self.id,
    	'name': self.name
    	}


class Item(Base):
    __tablename__ = 'items'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship(Category)

    @property
    def serialize(self):
    	return{
    	'name': self.name,
    	'id': self.id,
    	'description': self.description,
    	'category_id': self.category_id
    	}



engine = create_engine('sqlite:///itemcatalog.db')


Base.metadata.create_all(engine)