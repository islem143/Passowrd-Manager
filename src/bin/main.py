

from ..lib.Util import Util
from .Menus import vault_menu
from .Menus import account_menu


def main():

    while True:
        if(Util.is_connected()):
            account_menu()
        else:

            vault_menu()


main()
