from .. import GLOBAL
from .Menus import VaultMenu
#from .Menus import AccountMenu
from ..Models import setup
def main():
    
   
    if(GLOBAL["db"] is None):
         setup()
    while True:
        if GLOBAL["session"] is None:
            vault = VaultMenu()
            vault.init()
        else:
            #account = AccountMenu()
           # account.init()
           pass


main()
