import sqlite3


class BancoDados:
    def __init__(self) -> None:
        self.__nome = './dados/zurcBanco.db'
        self.conexao = None
        self.cursor = None

    def conectar(self) -> None:
        try:
            self.conexao = sqlite3.connect(self.__nome)
            self.cursor = self.conexao.cursor()
        except ConnectionError:
            print('Erro na conexão')

    def desconectar(self) -> None:
        try:
            self.conexao.close()
        except sqlite3.OperationalError:
            print('Erro ao desconectar-se')
