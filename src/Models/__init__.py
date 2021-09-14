from peewee import SqliteDatabase,Model,AutoField,CharField
from .Base import database,BaseModel
from .Vault import Vault




def setup():
    database.connect()
    with database:
        database.create_tables([Vault])
