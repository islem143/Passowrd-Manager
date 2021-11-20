from .Menu import Menu
from ..Controllers import Vault
from .AccountMenu import AccountMenu 

CHOICES = {
    "1": "create a database/vault",
    "2": "connect to a database/vault"
}


class VaultMenu(Menu):

    def init(self):
        vault = Vault()
        choices = [i for i in list(CHOICES.keys())]
        self.display_choices(CHOICES)
        choice = self.get_choice(choices)
        if(not choices):
            self.init()
        name = self.promt("enter the name of the vault")
        masterpassword = self.promt("enter the masterpassword", True)
        if(choice == "1"):
            vault.create_vault(name, masterpassword)
        elif(choice == "2"):
            if(vault.connect_to_vault(name, masterpassword)):
                 accountMenu=AccountMenu()
                 accountMenu.init()
                 


