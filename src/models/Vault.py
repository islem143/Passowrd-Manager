from sqlalchemy import Column,Integer,String,select
from .database import Base,db
from sqlalchemy.exc import SQLAlchemyError


class Vault(Base):
    __tablename__="vault"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    masterPassword = Column(String(200))
    salt=Column(String(200))

    def createVault(self,name,masterPassword,salt):
        vault=Vault(name=name,masterPassword=masterPassword,salt=salt)
        with db.getSession() as session:
              session.add(vault)
              session.commit()
              return True 
    def getVault(self,name,masterPassword):
                with  db.getSession() as session:
                    res=session.execute(select(Vault).where(Vault.name==name)).first()
                    session.commit()
                    print(res)

    def __repr__(self):
       return f"vault(id={self.id!r}, name={self.name!r},masterPassword={self.masterPassword!r}),salt={self.salt!r}"