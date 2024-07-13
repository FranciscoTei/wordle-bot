from peewee import SqliteDatabase, Model, CharField, IntegerField, BooleanField, DateField, ForeignKeyField, BigIntegerField, DateTimeField
import datetime
from zoneinfo import ZoneInfo

from wordle.messages import keyboard_layout

db = SqliteDatabase('wordle_teste.sqlite')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    user_id = BigIntegerField(null=False)
    name = CharField(max_length=100, null=False)
    username = CharField(max_length=40)
    created_at = DateTimeField(default=datetime.datetime.now)


class Word(BaseModel):
    user = ForeignKeyField(User, backref='words', null=False)
    text = CharField(max_length=5, null=False)
    creat_at = DateField(default=datetime.date.today)


class Game(BaseModel):
    user = ForeignKeyField(User, backref='jogos', null=False)
    word = ForeignKeyField(Word, backref='jogos', null=False)
    keyboard = CharField(default=keyboard_layout)
    state = BooleanField(default=True)
    data = DateField(default=datetime.date.today)

class Guess(BaseModel):
    user = ForeignKeyField(User, backref='tentativas', null=False)
    word = ForeignKeyField(Word, backref='tentativas', null=False)
    game = ForeignKeyField(Game, backref='tentativas', null=False)
    text = CharField(max_length=5, null=False)
    tip = CharField(max_length=255, null=True)

class Score(BaseModel):
    user = ForeignKeyField(User, backref='score', null=False, unique=True)
    pontos = IntegerField(default=0)
    jogos = IntegerField(default=0)
    vencidos = IntegerField(default=0)
    perdidos = IntegerField(default=0)
    desistencias = IntegerField(default=0)

if __name__ == "__main__":
    db.connect()
    db.drop_tables([User, Word, Game, Guess, Score])
    db.create_tables([User, Word, Game, Guess, Score])
