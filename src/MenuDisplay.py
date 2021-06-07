

class MenuDisplay:

    @staticmethod 
    def displayInit():
          MenuDisplay.display("Welcome to vault\n")
          MenuDisplay.display("Do you want To:\n")
          MenuDisplay.display("1-Create a Vault ?")
          MenuDisplay.display("2-Connect to an existing  Vault ?")
    @staticmethod
    def display(text):
        print(text)    
   