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
        except Exception as error:
            print(f'Houve um erro: {error}')

    def desconectar(self) -> None:
        try:
            self.conexao.close()
        except Exception as erro:
            print(f'Erro ao desconectar-se: {erro}')
