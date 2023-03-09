import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Myenum(enum.Enum):
    IMAGEN = "image"
    PDF = "pdf"
    MP4 = "mp4"




class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    firstname = Column(String(80))
    lastname = Column(String(80))
    email = Column(String(80))


class Folower(Base):
    __tablename__ = "folower"
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("user.id"))
    user_to_id = Column(Integer, ForeignKey("user.id"))
    user= relationship("user")


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    user =relationship("user")


class Comment(Base):
    __tablename__ = "comment"
    id= Column(Integer, primary_key=True)
    comment_text=Column(String(250))
    author_id = Column(Integer, ForeignKey("user.id"))  
    post_id =Column(Integer, ForeignKey("post.id"))
    user= relationship("user")


class Media(Base):
    __tablename__ ="media"
    id = Column(Integer, primary_key=True)
    type_=Column(Enum(Myenum))
    url= Column(String(60))
    post_id= Column(Integer, ForeignKey("post.id"))
    post = relationship("post")    
    




## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
