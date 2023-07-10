from modulos.dbsqlite import BancoDados
from modulos.fornecedor import Fornecedor
from modulos.produto import  Produto



class Fornecimento:
    # Construtor
    banco = BancoDados()
    fornecedor = Fornecedor()
    prod = Produto()

    def __init__(self, cnpj=None, cod_produto=None, qtd_fornecida=None, data_fornecimento=None) -> None:
        self.__cnpj = cnpj
        self.__cod_produto = cod_produto
        self.__qtd_fornecida = qtd_fornecida
        self.__data_fornecimento = data_fornecimento

    # Getters e Setters

    def get_cnpj(self) -> str:
        return self.__cnpj 

    def set_cnpj(self, cnpj) -> None:
        self.__cnpj = cnpj

    def get_cod_produto(self) -> int:
        return self.__cod_produto
    
    def set_cod_produto(self, cod_produto) -> None:
        self.__cod_produto = cod_produto

    def get_qtd_fornecida(self) -> int:
        return self.__qtd_fornecida

    def set_qtd_fornecida(self, qtd_fornecida: int) -> None:
        self.__qtd_fornecida = qtd_fornecida

    def get_data_fornecimento(self) -> str:
        return self.__data_fornecimento

    def set_data_fornecimento(self, data_fornecimento: str) -> None:
        self.__data_fornecimento = data_fornecimento

    

    def cadastrar_fornecimento(self, cnpj, cod_produto, qtd, data) -> None:
        self.banco.conectar()
        self.banco.cursor.execute(f"""INSERT INTO fornecimento(cod_produto, cod_fornecedor, data_fornecimento, qtd_fornecida)
                                  VALUES ('{cod_produto}'), ('{cnpj}'), ('{qtd}'), ('{data}') """)
        self.banco.conexao.commit()
        self.banco.desconectar()