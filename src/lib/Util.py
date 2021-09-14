


class Util:
       
       @staticmethod
       def is_password_valid(string,tocompare,method):
           return method(string,tocompare)