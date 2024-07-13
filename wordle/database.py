import pymysql
import json
from icecream import ic
ic.configureOutput(includeContext=True)
from wordle.messages import CHUTES
from rich.traceback import install
install(show_locals=True)
import datetime
import pytz
import sqlite3


tz = pytz.timezone('America/Sao_Paulo')

class DateTimeInfo:
    """
    Classe para obter informações de data e hora, incluindo o fuso horário de Brasília.
    """
    def __init__(self):
        self._atualizar_informacoes()

    def _atualizar_informacoes(self):
        dt = datetime.datetime.now(tz)
        self._hoje = dt.strftime("%Y-%m-%d")
        self._horario = dt.strftime("%H:%M:%S")
        self._data = dt.strftime("%Y-%m-%d %H:%M:%S")


    @property
    def hoje(self):
        self._atualizar_informacoes()
        return self._hoje

    @property
    def horario(self):
        self._atualizar_informacoes()
        return self._horario

    @property
    def data(self):
        self._atualizar_informacoes()
        return self._data

infodata = DateTimeInfo()


class DataBaseSQL:
    def __init__(self):
        """self.con = pymysql.connect(
            host='uyu7j8yohcwo35j3.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
            user='h2xwhmugacxbwv79',
            password='mfuwh70z5pjq0jwb',
            database='q6p5up8xhrrbmyq0'
        )
        self.cursor_dict = pymysql.cursors.DictCursor"""
        self.database = "wordle.sqlite"
        #self.cursor_dict = self.con.cursor()
        #self.con.row_factory = sqlite3.Row


    def executa(self, query):
        try:
            with sqlite3.connect(self.database) as con:
                con.row_factory = sqlite3.Row
                cursor = con.cursor()
                cursor.execute(query)
                resultado = cursor.fetchone()
                cursor.close()
                return resultado
        except pymysql.Error as error:
            ic(error)
            return error

    def update(self, query):
        try:
            with sqlite3.connect(self.database) as con:
                #con.row_factory = sqlite3.Row
                cursor = con.cursor()
                cursor.execute(query)
                con.commit()
                cursor.close()
        except Exception as error:
            ic(error)
        return True

    def delete(self, query):
        try:
            with sqlite3.connect(self.database) as con:
                con.row_factory = sqlite3.Row
                cursor = con.cursor()
                cursor.execute(query)
                con.commit()
                cursor.close()
        except pymysql.Error as error:
            return error
        return True
        
    def salva_jogador(self, nome: str, username: str, iduser: str, palavra: str):
        with sqlite3.connect(self.database) as con:
            con.row_factory = sqlite3.Row
            cursor = con.cursor()
            cursor.execute(
                "INSERT INTO wordle(nome, iduser, username, palavra, chutes, data, tentativas) VALUES(?, ?, ?, ?, ?, ?, ?)", [nome, iduser, username, palavra, CHUTES, infodata.hoje, 0]
            )
            con.commit()

            cursor.execute(
                f"SELECT * FROM wordle WHERE iduser = '{iduser}' AND data = '{infodata.hoje}' AND encerrado = 0"
            )
            resultado = cursor.fetchone()
            ic = resultado
            cursor.close()
            return resultado
            
    def select_dict(self, query):
        with sqlite3.connect(self.database) as con:
            con.row_factory = sqlite3.Row
            cursor = con.cursor()
            cursor.execute(query)
            return cursor.fetchone()

        
    def add_chutes(self, iduser):
        try:
            with sqlite3.connect(self.database) as con:
                con.row_factory = sqlite3.Row
                con.ping()

                cursor = con.cursor()
                cursor.execute(
                    "UPDATE wordle SET chutes = %s WHERE iduser = %s",[CHUTES, iduser]

                 )

                con.commit()
                cursor.close()
        except Exception as Error:
            ic(Error)
            
    def salva_chutes(self, chutes, iduser, tentativas):
        try:
            with sqlite3.connect(self.database) as con:
                con.row_factory = sqlite3.Row
                #self.con.ping()
                chutes = json.dumps(chutes)
                cursor = con.cursor()
                cursor.execute(
                    "UPDATE wordle SET chutes = ?, tentativas = ? WHERE iduser = ?", [chutes, tentativas, iduser]
                )
                con.commit()
                cursor.close()
                ic()
        except Exception as Error:
            ic(Error)

sql = DataBaseSQL()
#sql.add_chutes(5083676810)
#sql.update("ALTER TABLE wordle ADD encerrado INT DEFAULT 0")






    


