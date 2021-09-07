from ..Menu.Menu import Menu
from .VaultChoices import INIT_CHOICES
from .VaultActions import VaultActions


class VaultMenu(Menu):

    def __init__(self) -> None:
        super().__init__(INIT_CHOICES)

    def init(self):
        vault_actions = VaultActions()
        self.display()
        choice = self.get_choice()
        if(choice == "1"):
            name, masterpassword = self.promts([{"message": "enter the name of the vault", "hidden": False}, {
            "message": "enter the masterpassword",
            "hidden": True
        }])
            vault_actions.create_vault(name,masterpassword)
        elif(choice=="2"):
             name, masterpassword = self.promts([{"message": "enter the name of the vault", "hidden": False}, {
            "message": "enter the masterpassword",
            "hidden": True
             }])
             vault_actions.connect_to_vault(name,masterpassword)

