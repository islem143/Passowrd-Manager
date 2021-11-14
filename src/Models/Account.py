from peewee import CharField, AutoField, TextField
from .Base import BaseModel

class Account(BaseModel):

    id = AutoField()
    name = CharField()
    url=CharField()
    password=CharField()
    notes=TextField()

    
    def __repr__(self):
        return f"account(id={self.id!r}, name={self.name!r},masterPassword={self.url!r},password={self.password})"