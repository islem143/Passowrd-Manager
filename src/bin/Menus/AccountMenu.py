from ..Controllers.Account import Account
from .Menu import Menu

CHOICES = {
    "1": "create an Account",
    "2": "get an Account",
    "3": "list accounts"
}


def print_account_detail( account):
    print("------Account------")
    print(f"name: {account.name}")
    print(f"url: {account.url}")
    print(f"notes: {account.notes}")
    print(f"password: {account.password}")
    print()


def account_menu():
    account = Account()
    choices = [i for i in list(CHOICES.keys())]
    Menu.display_choices(CHOICES)
    choice = Menu.get_choice(choices)
    if(choice == "1"):
        name = Menu.promt("account name")
        url = Menu.promt("account url")
        password = Menu.promt("account password", True)
        notes = Menu.promt("account notes")
        account.create_account(name, url, password, notes)
    elif(choice == "2"):
        name = Menu.promt("account name")
        account = account.get_account(name)
        print_account_detail(account)
    elif(choice == "3"):
        accounts = account.list_accounts()
    # Menu.init()
