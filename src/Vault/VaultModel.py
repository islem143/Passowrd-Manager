from sqlalchemy import Column,Integer,String,select
from ..Database.Database import Base
from sqlalchemy.exc import SQLAlchemyError
from ..Database.Database import Database 
from sqlalchemy import select

class Vault(Base):
    __tablename__="vault"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    masterpassword = Column(String(200))
    salt=Column(String(200))
    
    @classmethod
    def get_vault(self):
        return select(Vault)


   



    

    def __repr__(self):
       return f"vault(id={self.id!r}, name={self.name!r},masterPassword={self.masterpassword!r})"