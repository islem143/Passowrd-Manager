
from peewee import DatabaseError, DoesNotExist
from ...Models import Vault as VaultModel
from ...lib import Hash
from ... import GLOBAL
from ...lib.Util import Util


class Vault:

    # def __init__(self) -> None:
    #     self.hash = Hash()

    def create_vault(self, name, masterpassowrd):

        hashedpassword, salt = Hash.hash(masterpassowrd)
        vault = VaultModel(name=name, masterpassword=hashedpassword, salt=salt)
        vault.save()
        print(f"vault created for {name} with {masterpassowrd}")
        return vault

    def compare_password(self, masterpassword, salt, hashedpassword):
        return Hash.compare(masterpassword, salt, hashedpassword)

    def connect_to_vault(self, name, masterpassword):
        try:
            vault = Vault.get_vault(name)
            if(not self.compare_password(masterpassword, vault.salt, vault.masterpassword)):
                print(f"Invalid password for{name}")
                return False
            print(f"Login successfully for vault {name}")
            Util.set_global("key", vault.masterpassword)
            Util.set_global("user", vault.name)
            return True

        except DoesNotExist as e:
            print(f"Vault: {name} does not exists")
            return

    @classmethod
    def get_vault(self, name):
        vault = VaultModel.get(VaultModel.name == name)
        return vault
