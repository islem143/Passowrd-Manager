from .VaultModel import Vault as VaultModel
from ..Database.Database import Database

import bcrypt

class Vault:
      db=Database("test")
      def __init__(self,name,masterpassword):
          self.name=name
          self.masterpassword=masterpassword
          
          Vault.db.create_db()
          #self.vault=VaultModel(name=name,masterpassword=masterpassword)


      def hash(self):
          salt=bcrypt.gensalt()
          hashedpassword=bcrypt.hashpw(self.masterpassword.encode(),salt)
          return (hashedpassword,salt)
          
      def save(self,hashedpassword,salt):
          vault=VaultModel(name=self.name,masterpassword=hashedpassword,salt=salt)
          with self.db.get_session() as session:
              session.add(vault)
              session.commit()
              
      @classmethod
      def connect(cls,name,masterpassword):
           with cls.db.get_session() as session:
              vault=session.execute(VaultModel.get_vault()).first()
              return vault
              
     