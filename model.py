from database import Base,engine
from sqlalchemy import Column,Integer,String
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,index=True)
    description = Column(String)


