import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User (Base):
    __tablename__ = 'User'
    id = Column (Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone_number = Column(Integer, nullable=False)

class Followers (Base):
    __tablename__ = 'Followers'
    id = Column (Integer, primary_key=True)
    from_user = Column(Integer, ForeignKey('User.id') )
    to_user = Column(Integer, ForeignKey('User.id') )

class Post (Base):
    __tablename__ = 'Post'
    id = Column (Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey('User.id'))
    type = Column(String, nullable=False)

class Comments (Base):
    __tablename__ = 'Comments'
    id = Column (Integer, primary_key=True)
    email = Column(String(250), nullable=True)
    post_id = Column (Integer, ForeignKey('Post.id'))
    user_id = Column (Integer, ForeignKey('User.id'))
    
class Likes (Base):
    __tablename__ = 'Likes'
    id = Column (Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    no_of_likes = Column(Integer, nullable=True)
    user_id = Column (Integer, ForeignKey('User.id'))
    post_id = Column (Integer, ForeignKey('Post.id'))




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
