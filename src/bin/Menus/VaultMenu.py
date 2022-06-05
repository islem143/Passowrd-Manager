
from ..Controllers import Vault
from .AccountMenu import account_menu
from .Menu import Menu
CHOICES = {
    "1": "create a database/vault",
    "2": "connect to a database/vault"
}

PROMTS = {
    "name": ["enter the name of the vault", False],
    "passowrd": ["enter the masterpasswor", True]
}


def vault_menu():

    choices = [i for i in list(CHOICES.keys())]
    Menu.display_choices(CHOICES)
    choice = Menu.get_choice(choices)
    if(not choice):

        return
    name = Menu.promt("enter the name of the vault")
    masterpassword = Menu.promt("enter the masterpassword", True)
    vault = Vault()
    if(choice == "1"):

        vault.create_vault(name, masterpassword)

    elif(choice == "2" and vault.connect_to_vault(name, masterpassword)):
        pass

        #accountMenu = AccountMenu()
    # accountMenu.init()
