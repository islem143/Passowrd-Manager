from ..Controllers.Account import Account
from .Menu import Menu
from  tabulate import tabulate
CHOICES = {
    "1": "Create an Account",
    "2": "Get an Account",
    "3": "List accounts"
}


def print_account_detail(account):
    print("------Account------")
    print(f"Name: {account.name}")
    print(f"Url: {account.url}")
    print(f"Notes: {account.notes}")
    print(f"Password: {account.password}")
    print()

def print_accounts(accounts):
    accounts=[[account.name,account.url,account.notes] for account in accounts]
    print(tabulate(accounts, headers=["Name","Url","notes"]))
    
    
def account_menu():
    account = Account()
    choices = [i for i in list(CHOICES.keys())]
    Menu.display_choices(CHOICES)
    choice = Menu.get_choice(choices)
    if (choice == "1"):
        name = Menu.promt("Account name ")
        url = Menu.promt("Account url ")
        password = Menu.promt("Account password ", True)
        notes = Menu.promt("Account notes ")
        account.create_account(name, url, password, notes)
    elif (choice == "2"):
        name = Menu.promt("Account name ")
        account = account.get_account(name)
        if (account):
            print_account_detail(account)
    elif (choice == "3"):
        accounts = account.list_accounts()
        if (len(accounts) != 0):
            print_accounts(accounts)
