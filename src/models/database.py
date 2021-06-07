from sqlalchemy import create_engine
from sqlalchemy.orm import Session,declarative_base
Base=declarative_base()

class Database:

    def __init__(self,database):
     self.engine=create_engine(database)
 
    def getEngine(self):
        """
        create a db engine and return it

        """
        
        return self.engine

    def getSession(self):
        """
        return a Session
        
        Returns

        -------
        Session
           a seiison  
        """
        return Session(bind=self.engine)
        
    def createDb(self):
        """
        create the Database 

        """
        self.getSession
        session=self.getSession()
        with session as s:
           Base.metadata.create_all(self.engine)
           s.commit()

dbStr="sqlite+pysqlite:///dbfile1.db"
db=Database(dbStr)  