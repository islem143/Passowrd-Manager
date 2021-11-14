from ..Controllers.Account import Account
from .Menu import Menu

CHOICES={
        "1":"create an Account",
        "2":"get an Account",
        }


class AccountMenu(Menu):

   
    def init(self):
        account = Account()
        choices = [i for i in list(CHOICES.keys())]
        self.display_choices(CHOICES)
        choice=self.get_choice(choices)

        di = {
            "1": account.create_vault,
            "2": account.connect_to_vault
        }
     
 
        
     

    