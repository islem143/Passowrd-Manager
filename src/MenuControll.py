from getpass import getpass
from  .MenuDisplay import MenuDisplay
from .Validation import Validation
class MenuControll:
    validation=Validation()
    def getInput(self,promt,Type=None):
        if(Type=="password"):
           res=getpass(promt) 
        else :
            res=input(promt)
        return res

    def initPromt(self):
        while True:
               res=self.getInput("Enter 1 Or 2:")
               if(res.strip()=="1"):
                   return "1"
               elif(res.strip()=="2"):
                    return "2"
               else: 
                    MenuDisplay.display("Please enter 1 Or 2:")
    def newVaultPromt(self):
         MenuDisplay.display("Please enter the name of the vault")
         vaultName=self.getInput("Name of the Vault:")
         while True:
               MenuDisplay.display("Please enter master massword")
               masterPassword=self.getInput("Master password:","password")
               cMasterPassowrd=self.getInput("Confirm master password:","password")
               isMatch=self.validation.confirmMasterPassword(masterPassword,cMasterPassowrd)
               if(isMatch and self.validation.isMasterPasswordValid(masterPassword)):
                   return [vaultName,masterPassword]
