from src.Account.Account import Account
from src.Vault.VaultMenu import VaultMenu
from src.Session import SESSIONS


def main():
    while True:
        if len(SESSIONS)==0:
            vault = VaultMenu()
            vault.init()
        else:
            account=Account()
            print(account.display())






main()


