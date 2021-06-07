import os 
from src.models.database import db
from src.Menu import Menu
from src.models.Vault import Vault
from src.models.Accounts import Accounts

def main():
    if(not os.path.isfile("dbfile1.db")):
        db.createDb()    
    menu=Menu()
    menu.init()
    
    
   
   


   



if __name__=="__main__":
  main()