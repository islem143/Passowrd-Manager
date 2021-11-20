from peewee import SqliteDatabase, Model
from .. import GLOBAL


GLOBAL["db"] = "test.db"
database = SqliteDatabase(GLOBAL["db"])
database.connect()


class BaseModel(Model):
    class Meta:
        database = database

from .Vault import Vault
from .Account import Account
with database:
    database.create_tables([Vault,Account])
