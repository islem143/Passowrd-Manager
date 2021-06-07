from .MenuControll import MenuControll
from .MenuDisplay import MenuDisplay
from .models.Vault  import Vault as Vaultdb
from .Hash import Hash

class Vault:
     menuControll=MenuControll()
     def createNewVolt(self): 
          [vaultName,masterPassword]=self.menuControll.newVaultPromt()
          hash=Hash()
          [hashedPassword,salt]=hash.hash(masterPassword)
          vault=Vaultdb()
          vault.createVault(name=vaultName,masterPassword=hashedPassword,salt=salt)
            

     def connect(self):
          MenuDisplay.display("pleast enter the name")
          vaultName=self.menuControll.getInput("Name of the Vault:")
          MenuDisplay.display("Please enter master massword")
          masterPassword=self.menuControll.getInput("Master password:","password")
          vault=Vaultdb()
          vault.getVault(vaultName,masterPassword)
                
                   

                    
                    








                    


                    
                    
               
              

