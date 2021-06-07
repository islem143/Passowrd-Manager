from sqlalchemy import Column,Integer,String
from .database import Base

class Accounts(Base):
    __tablename__="accounts"
    id = Column(Integer, primary_key=True)
    login = Column(String(30))
    Password = Column(String(50))
    url=Column(String(50))
    site=Column(String(50))
    
    def __repr__(self):
       return f"accounts(id={self.id!r}, name={self.login!r})"