from  .MenuDisplay import MenuDisplay
import re
class Validation:

    def confirmMasterPassword(self,masterPassword,cMasterPassword):
        if(masterPassword!=cMasterPassword):
            MenuDisplay.display("No matching passwords")
            return False
        return True

    def isMasterPasswordValid(self,masterPassword):
        if(len(masterPassword.strip())<8):
           MenuDisplay.display("The Password should be at least 8 characters length")
           return False
        regx="^([a-zA-Z])(?=.*\d)(?=.*[$@#%])[a-zA-Z\d$@#%]*$"
        if (not re.search(regx,masterPassword)):
            MenuDisplay.display("password should start with an alphabet and conaitans alphanumric and one of this sympols")
            MenuDisplay.display("[$ @ # %]")
            return False
        return True    