from modulos.dbsqlite import BancoDados

banco = BancoDados()

class Servico:
    # Construtor
    def __init__(self, cod_servico: str=None, descricao_servico: str=None, preco_servico: float=None, tipo: str=None) -> None:
        # Atributos (privado)
        self.__cod_servico = cod_servico
        self.__descricao_servico = descricao_servico
        self.__preco_servico = preco_servico
        self.__tipo = tipo

    # Getters e Setters
    def get_cod_servico(self) -> str:
        return self.__cod_servico

    def set_cod_servico(self, cod_servico:str) -> None:
        self.__cod_servico = cod_servico

    def get_descricao_servico(self) -> str:
        return self.__descricao_servico

    def set_descricao_servico(self, descricao:str) -> None:
        self.__descricao_servico = descricao

    def get_preco_servico(self) -> float:
        return self.__preco_servico

    def set_preco_servico(self, preco:float) -> None:
        self.__preco_servico = preco

    def get_tipo(self) -> str:
        return self.__tipo

    def set_tipo(self, tipo:str) -> None:
        self.__tipo = tipo


    def cadastrarServico(self, codigo:str, descricao:str, preco:float, tipo:float) -> None:
        banco.conectar()
        try:
            banco.cursor.execute(f"""INSERT INTO servico(cod_servico, descricao_servico, preco_servico, tipo)
            VALUES ('{codigo}', '{descricao}', '{preco}', '{tipo}')""")
            banco.conexao.commit()
            banco.desconectar()
        except:
            print('Erro')

    def listarServicos(self) -> list:
        banco.conectar()
        try:
            servicos = banco.cursor.execute(f"""SELECT * FROM servico """).fetchall()
            banco.desconectar()
            return servicos
        except ConnectionError:
            print('Nenhum produto encontrado')

    def alterarServico(self, cod_servico:str, descricao:str, preco:float, tipo:str) -> None:
        banco.conectar()
        banco.cursor.execute(f"""UPDATE servico                     
                                 SET descricao_servico = '{descricao}',
                                 preco_servico = '{preco}',
                                 tipo = '{tipo}'
                                 WHERE cod_servico ='{cod_servico}'""")
        banco.conexao.commit()
        banco.desconectar()

    def excluirServico(self, cod_servico:str) -> None:
        banco.conectar()
        banco.cursor.execute(f"""DELETE FROM servico WHERE cod_servico = '{cod_servico}' """)
        banco.conexao.commit()
        banco.desconectar()