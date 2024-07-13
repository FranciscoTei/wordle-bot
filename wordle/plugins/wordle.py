from wordle.models import User, Word, Game, Guess, Score
import random
import datetime
from wordle.messages import CHUTE_INVALIDO, keyboard_dict
from novaspalavras import nova_lista as wordleDictionary
from wordle.palavras.dict_1500 import dicicionario1500
from unidecode import unidecode

from collections import Counter


id_message_estranhas = 0

class Wordle:
    def __init__(self):
        self.palavras_estranhas = []

    def check_new_user(self, usuario):
        return User.select().where(User.user_id == usuario.id).first()

    def create_user(self, usuario):
        user = User.create(user_id=usuario.id, name=usuario.first_name, username=usuario.username)
        user.save()
        Score.create(user=user).save()

    def get_position(self, user_score):
        position = (Score
            .select(Score, User)
            .join(User)
            .where(Score.pontos > user_score)
            .count() + 1)

        return position
    
    def get_ranking(self):
        ranking = (Score
            .select(Score, User)
            .join(User)).order_by(Score.pontos.desc())
        return ranking

    def get_user(self, usuario):
        return User.select().where(User.user_id == usuario.id).get()

    def get_word(self):
        return 

    def new_wordle(self, usuario):
        user = self.get_user(usuario)
        word = Word.create(user=user, text=get_new_word())
        word.save()

        game = Game.create(user=user, word=word)
        game.save()
        return game


    # static mode
    def validate_guess(self, guess):
        if not len(guess) == 5:
            return {'validate': False, 'detail': CHUTE_INVALIDO}
        elif guess.lower() not in wordleDictionary:
            return {'validate': True}
            self.palavras_estranhas.append(guess.lower())
            return {'validate': False, 'detail': "A palavra deve ser uma palavra válida do português brasileiro."}
        return {'validate': True}

    def get_last_game(self, usuario):
        today = datetime.date.today()
        game: Game = Game.select().join(User).where(User.user_id == usuario.id, Game.data == today, Game.state == 1).first()


        if game:
            return game
        else:
            return self.new_wordle(usuario)

    
    def response_guess(self, usuario, guess_text):
        game = self.get_last_game(usuario)
        if game.state:
            word = game.word
            user = self.get_user(usuario)
            guess = Guess.create(user=user, word=word, game=game, text=guess_text)


            guess_hint = '01234'
            letter_counts = Counter(word.text)
            for i, letter in enumerate(guess.text):
                if letter == word.text[i]:
                    guess_hint = guess_hint.replace(f"{i}","🟩")
                    letter_counts[letter] -= 1
                    game.keyboard = game.keyboard.replace(keyboard_dict[letter][0], keyboard_dict[letter][1])
                    game.save()

            for i, letter in enumerate(guess.text):        
                if letter in word.text and letter_counts[letter] > 0:
                    guess_hint = guess_hint.replace(f"{i}","🟨")
                    letter_counts[letter] -= 1
                    game.keyboard = game.keyboard.replace(keyboard_dict[letter][0], keyboard_dict[letter][1])
                    game.save()
                else:
                    game.keyboard = game.keyboard.replace(keyboard_dict[letter][0], "—")
                    game.save()
                    guess_hint = guess_hint.replace(f"{i}","🟥")

            guess.tip = guess_hint
            guess.save()


            today = datetime.date.today()
            attempts = user.tentativas.select().join(Game).where(Game.data == today, Game.state == 1)

            response = '<b>WORDLE LOBINDIE</b>\n\n'
            for attempt in attempts:
                response += f" <code>{' '.join(attempt.text)}</code>\n"
                response += f"{attempt.tip}\n"
            response += (6-len(attempts))*'🟦🟦🟦🟦🟦\n'  + '\n' + game.keyboard

            if guess.text == word.text:
                game.state = False
                game.save()
                Score.update(
                    pontos=Score.pontos + (7 - len(attempts)),
                    jogos=Score.jogos + 1,
                    vencidos=Score.vencidos + 1
                ).where(
                    Score.id == user.id
                ).execute()
    
                return [response, f"\n\nParabéns! Você acertou a palavra e ganhou {7 - len(attempts)} pontos."]
            if len(attempts) == 6:
                game.state = False
                game.save()
                Score.update(
                    jogos=Score.jogos + 1,
                    perdidos=Score.perdidos + 1
                ).where(
                    Score.id == user.id
                ).execute()
                return [response, f"\n\nInfelizmente você perdeu. A palavra era <b>{word.text}</b>"]
            return [response]


        elif not game.state:
            return ["Você não tem mais palavras para hoje. Volte amanhã."]

        #guess = Guess.create(user=usuario, word=self.get_word(usuario), game=game, text='berco', tip='errado')




def get_new_word():
    word = random.choice(dicicionario1500)
    return unidecode(word.upper())

wordle_jogo = Wordle()