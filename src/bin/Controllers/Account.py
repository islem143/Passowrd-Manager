from peewee import DoesNotExist

from ...globals import GLOBAL
from ...Models.Account import Account as AccountModel
from ...lib.Encryption import Encryption


class Account:

    def create_account(self, name, url, password, notes):
        key = GLOBAL["key"]
        key += GLOBAL["user"]
        enc = Encryption(key)
        password = enc.encrypt(password.encode())
        account = AccountModel(
            name=name, url=url, password=password, notes=notes)

        account.save()
        return account
        print(f"account {name} created ")

    def print_account_detail(self, account):
        print("------Account------")
        print(f"name: {account.name}")
        print(f"url: {account.url}")
        print(f"notes: {account.notes}")
        print(f"password: {account.password}")
        print()

    def get_account(self, name):
        try:
            account = AccountModel.get(AccountModel.name == name)
            key = GLOBAL["key"]
            key += GLOBAL["user"]
            enc = Encryption(key)
            password = enc.decrypt(account.password)
            account.password = password[1]
            return account

        except DoesNotExist:
            print()
            print(f"account {name} does not exits")
            print()
            return None

    def list_accounts(self):
        # To do add where vault is the current vault
        accounts = [account for account in AccountModel.select()]
        
            
        return accounts
