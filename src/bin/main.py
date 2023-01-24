

from ..lib.Util import Util
from .Menus import vault_menu
from .Menus import account_menu
import os
from art import text2art

def main():
    art=text2art("Welcome")
    print(art)
    while True:
        if (Util.is_connected()):

            account_menu()
        else:

            vault_menu()


main()
