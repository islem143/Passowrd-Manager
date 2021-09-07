import bcrypt


class Hash:

    def hash(self,string):
          salt=bcrypt.gensalt()
          hashedpassword=bcrypt.hashpw(string.encode(),salt)
          return (hashedpassword,salt)