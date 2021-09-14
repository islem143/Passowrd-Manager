from .Menu import Menu
from ..Controllers import Vault


CHOICES = {
    "1": "create a database/vault",
    "2": "connect to a database/vault"
}


class VaultMenu(Menu):

    def init(self):
        vault = Vault()
        choices = [i for i in list(CHOICES.keys())]
        self.display_choices(CHOICES)
        di = {
            "1": vault.create_vault,
            "2": vault.connect_to_vault
        }
        choice = self.get_choice(choices)

        if choice in choices:
            name = self.promt("enter the name of the vault")
            masterpassword = self.promt("enter the masterpassword",True)
            di[choice](name, masterpassword)
