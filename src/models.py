# from flask_sqlalchemy import SQLAlchemy
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
# db=SQLAlchemy()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    mail = Column(String(250), unique= True, nullable=False)
    age = Column(String(250), nullable=False)
    image = Column(String(250), nullable=False)

    posts = relationship("post", uselist=False, back_populates="user")
    comments = relationship("comment", uselist=False, back_populates="user")

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    user_from_id = Column(Integer,ForeignKey("user.id"))
    user_to_id = Column(Integer,ForeignKey("user.id"))

    users = relationship("user", uselist=False, back_populates="followers")


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    image =  Column(String(250),nullable=False)
    text =  Column(String(250),nullable=False)

    user = relationship("user", back_populates="post")
    comments = relationship("comment", uselist=False, back_populates="posts")

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    author_comment_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    text =  Column(String(250), nullable=False)

    user = relationship("user", back_populates="comments")
    post = relationship("post", back_populates="comments")



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e