import bcrypt

password=b'islem'     
salt=bcrypt.gensalt()
print(salt)
hashed=bcrypt.hashpw(password,salt)
# password2=b"islem"
# hashed2=bcrypt.hashpw(password2,salt)
print(bcrypt.checkpw(b"islem",hashed))
