
from ..Controllers.Account import Account
from .Menu import Menu

CHOICES = {
    "1": "create an Account",
    "2": "get an Account",
    "3":"list accounts"
}


class AccountMenu(Menu):

    def init(self):
        account = Account()
        choices = [i for i in list(CHOICES.keys())]
        self.display_choices(CHOICES)
        choice = self.get_choice(choices)
        if(choice == "1"):
                name = self.promt("account name")
                url = self.promt("account url")
                password = self.promt("account password", True)
                notes = self.promt("account notes")
                account.create_account(name, url, password, notes)
        elif(choice == "2"):
            name = self.promt("account name")
            account.get_account(name)        
        elif(choice == "3"):
            account.list_accounts() 
            