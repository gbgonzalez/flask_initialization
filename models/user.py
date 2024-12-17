from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    """
    This module defines a SQLAlchemy ORM (Object Relational Mapping) model for a 'User' table in a relational database.

    Classes:
    - User: Represents the 'user' table in the database.

    Attributes:
    - Base: A declarative base class used to define the structure of the ORM models.

    Class: User
    -----------
    The `User` class represents a table named 'user' in the database. It is designed to map the table structure into an object-oriented format that SQLAlchemy can interact with.

    Attributes:
    - __tablename__: str
        The name of the database table, which is 'user'.
    - id: Column
        An integer column that serves as the primary key for the table.
    - name: Column
        A string column to store the name of the user.
    - email: Column
        A string column to store the email address of the user.
    - password: Column
        A string column to store the user's password.
    """
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def to_dict(self):
        """
        Converts the User instance into a dictionary representation.

        Returns:
        dict: A dictionary containing the key-value pairs of the User object's attributes.
        """
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }