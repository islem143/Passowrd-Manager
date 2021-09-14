from peewee import SqliteDatabase,Model
from .. import GLOBAL

database=SqliteDatabase(GLOBAL["db"])

class BaseModel(Model):
    class Meta:
        database=database
