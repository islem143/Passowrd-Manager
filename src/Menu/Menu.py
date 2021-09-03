

class Menu:
    
    def __init__(self,choices) -> None:
      
        self.choices=choices
     
        
    
    def display(self):
         for (i,q) in self.choices.items():
            print(f"{i}-{q}")


    def get_choice(self):
           res=input("choose an option")
           for c in self.choices.keys():
               if str(c)==str(res):
                 return str(c)
           print("please enter a valid choice")
           return self.get_choice()


    def promts(self,promts):
        responces=[]
        for promt in promts:
            res=input(promt["message"])
            responces.append(res)

        return responces    

        

        
            
  
        

