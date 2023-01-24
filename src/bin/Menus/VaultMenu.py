
from ..Controllers import Vault
from .AccountMenu import account_menu
from .Menu import Menu
CHOICES = {
    "1": "Create a database/vault",
    "2": "Connect to a database/vault"
}

PROMTS = {
    "name": ["Enter the name of the vault", False],
    "passowrd": ["Enter the masterpasswor", True]
}


def vault_menu():

    choices = [i for i in list(CHOICES.keys())]
    Menu.display_choices(CHOICES)
    choice = Menu.get_choice(choices)
    if (not choice):

        return
    name = Menu.promt("Enter the name of the vault ")
    masterpassword = Menu.promt("Enter the masterpassword ", True)
    vault = Vault()
    if (choice == "1"):

        vault.create_vault(name, masterpassword)

    elif (choice == "2"):
        vault.connect_to_vault(name, masterpassword)

        # accountMenu = AccountMenu()
    # accountMenu.init()
