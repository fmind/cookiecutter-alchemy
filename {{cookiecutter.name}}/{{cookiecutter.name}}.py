#!/usr/bin/env python3

"""Declarative model of the project."""

from sqlalchemy import schema, types

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base

# CONFIGS

URL = 'sqlite:///:memory:'

# ENGINES

ENGINE = create_engine(URL, echo=True)

SESSION = sessionmaker(bind=ENGINE)()

# DEFINES

Base = declarative_base()

class User(Base):
    """A user of the system."""
    __tablename__ = 'users'

    id = schema.Column(types.Integer, primary_key=True)
    firstname = schema.Column(types.String)
    lastname = schema.Column(types.String)

    def __repr__(self):
        return f"<User(firstname='{self.firstname}', lastname='{self.lastname}')>"

# CREATIONS

Base.metadata.drop_all(ENGINE)
Base.metadata.create_all(ENGINE)

# INSERTIONS

carrie = User(firstname="Carrie-Anne", lastname="Moss")

keanu = User(firstname="Keanu", lastname="Reeves")

SESSION.add_all([carrie, keanu,])

SESSION.commit()

# SELECTIONS

for user in SESSION.query(User).all():
    print(user)
