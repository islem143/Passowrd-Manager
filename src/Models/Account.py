from peewee import CharField, AutoField, TextField
from . import BaseModel


class Account(BaseModel):

    id = AutoField()
    name = CharField()
    url = CharField()
    password = CharField()
    notes = TextField()

    def __repr__(self):
        return f"account(id={self.id!r}, name={self.name!r},url={self.url!r},password={self.password})"
