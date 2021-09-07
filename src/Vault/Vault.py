from .VaultModel import Vault as VaultModel
from ..Database.Database import Database
from ..Hash.Hash import Hash
from ..Session import SESSIONS,DATABASES
class Vault:
      
      def __init__(self,name,masterpassword):
          self.name=name
          self.masterpassword=masterpassword
          self.db=Database(name)
          
          
      def init(self):
         self.db.create_db()

      def hash(self):
          hash=Hash()
          return hash.hash(self.masterpassword)

      def is_password_valid(self,password,to_compare):
           hash=Hash()
           return hash.compare(password,to_compare)
              
      def save(self,hashedpassword,salt):
          vault=VaultModel(name=self.name,masterpassword=hashedpassword,salt=salt)
          with self.db.get_session() as session:
              session.add(vault)
              session.commit()
              
     
      def get_vault(self):
           db=Database(self.name)
           with db.get_session() as session:
              vault=session.execute(VaultModel.get_vault()).first()
              return vault
              
     