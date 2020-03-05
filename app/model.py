from mongoengine import *


class Users(Document):
    username = StringField(max_length=60, required=True)
    password = StringField(max_length=60, required=True)


class Messages(Document):
    username = StringField(max_length=60, required=True)
    messages = ListField()