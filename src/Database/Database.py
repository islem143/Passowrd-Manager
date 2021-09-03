from sqlalchemy import create_engine
from sqlalchemy.orm import Session,declarative_base
Base=declarative_base()

class Database:

    def __init__(self,name):
     db=f"sqlite+pysqlite:///{name}.db"
     self.engine=create_engine(db)
 
    def get_session(self):
        """
        return a Session
        
        Returns
        -------
        Session
           a session
        """
        return Session(bind=self.engine)
        
    def create_db(self):
        """
        Create the Database 
        """
        session=self.get_session()
        with session as s:
           Base.metadata.create_all(self.engine)
           s.commit()


