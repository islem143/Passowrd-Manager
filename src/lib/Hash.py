import hashlib
import uuid


class Hash:
    """
    A class used to hash passwords using sha246

    ...
    Attributes
    ----------

    Methods
    -------
    hash(string:str)-> tuple(hashed,salt)
         hash a string
    """

    @classmethod
    def hash(self, string: str) -> tuple:
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
        salt = uuid.uuid4().hex
        hash = hashlib.sha256(salt.encode()+string.encode()).hexdigest()

        return (hash, salt)

    @classmethod
    def compare(self, string: str, salt: str, hash: str) -> bool:
        """
        compare a password to it hash

        Parameters
        ----------
          string : str
             the string to be hashed
          to_compare: : str
             the hashed string

        Returns
        -------
          bool
             True if the string match to to_compare hashed value 
        """
        return hash == hashlib.sha256(salt.encode()+string.encode()).hexdigest()
