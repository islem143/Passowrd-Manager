import bcrypt

class Hash:
      
      def hash(self,password):
          password=str.encode(password)
          salt=bcrypt.gensalt()
          
          return [bcrypt.hashpw(password,salt).decode(),salt.decode()]

      def compare(self):
          
          pass  
