from .Vault import Vault
from ..Session import SESSIONS


class VaultActions:

    def create_vault(self, name, masterpassowrd):
        vault = Vault(name, masterpassowrd)
        hashedpassword, salt = vault.hash()
        vault.save(hashedpassword, salt)
        print(f"vault created for {name} with {masterpassowrd}")

    def connect_to_vault(self, name, masterpassword):
        vault = Vault.connect(name, masterpassword)
        SESSIONS.append(vault)
