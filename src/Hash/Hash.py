import bcrypt


class Hash:

    def hash(self,string):
          salt=bcrypt.gensalt()
          hashedpassword=bcrypt.hashpw(string.encode(),salt)
          return (hashedpassword,salt)

    def compare(self,string,to_compare):
        return bcrypt.checkpw(string,to_compare)
