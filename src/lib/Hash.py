import bcrypt


class Hash:
    """
    A class used to hash passwords using bcrypt pakcage

    ...
    Attributes
    ----------

    Methods
    -------
    hash(string:str)-> tuple(hashed,salt)
         hash a string
    """



    def hash(self,string:str) -> tuple:
          """
          Hash a given sring
          Parameters
          ----------
          string : str
             the string to be hashed

          Returns
          -------
          tuple
             a tuple which contains the hashed string and it salt  
          """

          salt=bcrypt.gensalt()
          hashedpassword=bcrypt.hashpw(string.encode(),salt)
          return (hashedpassword,salt)

    def compare(self,string:str,to_compare:bytes) -> bool:
        """
        compare a password to it hash

        Parameters
        ----------
          string : str
             the string to be hashed
          to_compare: : bytes
             the hashed string
            
        Returns
        -------
          bool
             True if the string match to to_compare hashed value 
        """
        return bcrypt.checkpw(string,to_compare)
