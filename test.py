import bcrypt

password=b'islem'     
salt=bcrypt.gensalt()
hashed=bcrypt.hashpw(password,b'$2b$12$SLiGxl.1RlLzQJfX6qZmjO')

print(b'$2b$12$SLiGxl.1RlLzQJfX6qZmjOgFItk73gSY8TeN0as2iakJHJXqKmGkm'==b'$2b$12$SLiGxl.1RlLzQJfX6qZmjOgFItk73gSY8TeN0as2iakJHJXqKmGkm')

#print(bcrypt.checkpw(password,hashed))