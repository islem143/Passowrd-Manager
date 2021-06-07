from  .MenuControll import MenuControll
from  .MenuDisplay import MenuDisplay
from  .Validation import Validation
from  .Vault import Vault
class Menu:
     menuControll=MenuControll()
     def init(self):
          MenuDisplay.displayInit()
          res=self.menuControll.initPromt()
          vault=Vault()
          if(res=="1"):
               vault.createNewVolt()
               return
          elif(res=="2"):
               vault.connect()
               return    
         

          


               
           
     
     


          

     

    

