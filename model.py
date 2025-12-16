from database import Base,engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    todos = relationship("Todo", back_populates="owner")

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,index=True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="todos")


