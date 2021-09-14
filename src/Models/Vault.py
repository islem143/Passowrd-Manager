from peewee import CharField, AutoField
from .Base import BaseModel


class Vault(BaseModel):

    id = AutoField()
    name = CharField()
    masterpassword = CharField()
    salt = CharField()

    def __repr__(self):
        return f"vault(id={self.id!r}, name={self.name!r},masterPassword={self.masterpassword!r})"