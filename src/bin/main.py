from .. import GLOBAL
from .Menus import VaultMenu
#from .Menus import AccountMenu


def main():
    while True:
        vault = VaultMenu()
        vault.init()


main()
