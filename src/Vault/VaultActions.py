from .Vault import Vault
from ..Database.Database import Database
from ..Session import SESSIONS
class VaultActions:

    def create_vault(self, name, masterpassowrd):
        vault = Vault(name, masterpassowrd)
        vault.init()
        hashedpassword, salt = vault.hash()
        vault.save(hashedpassword, salt)
        print(f"vault created for {name} with {masterpassowrd}")

    def connect_to_vault(self, name, masterpassword):
        vault = Vault(name, masterpassword)
        vault_info = vault.get_vault()[0]
        is_password_valid=vault.is_password_valid(masterpassword.encode(),vault_info.masterpassword)
        if(is_password_valid):
            SESSIONS.append(vault)
        else:
            print("invalid password")    
