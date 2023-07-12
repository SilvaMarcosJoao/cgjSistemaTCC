from modulos.dbsqlite import BancoDados
from modulos.fornecedor import Fornecedor
from modulos.produto import  Produto



class Fornecimento:
    # Construtor
    banco = BancoDados()
    fornecedor = Fornecedor()
    prod = Produto()

    def __init__(self, cod_fornecedor=None, cod_produto=None, qtd_fornecida=None, data_fornecimento=None) -> None:
        self.__cod_fornecedor= cod_fornecedor
        self.__cod_produto = cod_produto
        self.__qtd_fornecida = qtd_fornecida
        self.__data_fornecimento = data_fornecimento

    # Getters e Setters

    def get_cod_fornecedor(self) -> int:
        return self.__cod_fornecedor 

    def set_cnpj(self, cod_fornecedor) -> None:
        self.__cod_fornecedor = cod_fornecedor

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

    

    def cadastrar_fornecimento(self, cod_produto, cod_fornecedor, data, qtd) -> None:
        self.banco.conectar()
        self.banco.cursor.execute(f"""INSERT INTO fornecimento (cod_produto, cod_fornecedor, data_fornecimento, qtd_fornecida)
                                  VALUES ('{cod_produto}', '{cod_fornecedor}', '{data}', '{qtd}')""")
        self.banco.conexao.commit()
        self.banco.desconectar()
    
    def listar_fornecimento(self) -> list:
        self.banco.conectar()
        forneci = list(self.banco.cursor.execute(f""" SELECT produto.desc_produto, fornecedor.nome_fornecedor, data_fornecimento, qtd_fornecida 
                                                 FROM produto, fornecedor, fornecimento
                                                 WHERE fornecimento.cod_produto = produto.cod_produto and 
                                                 fornecimento.cod_fornecedor = fornecedor.cod_fornecedor""").fetchall())
        self.banco.conexao.commit()
        self.banco.desconectar()
        return forneci
    
    def alterar_fornecimento(self, cod_produto, cod_fornecedor):
        self.banco.conectar()
        self.banco.cursor.execute(f""" UPDATE fornecimento SET qtd_fornecida, data_fornecimento
                                  WHERE cod_produto = '{cod_produto}' and cod_fornecedor = '{cod_fornecedor}' """)
        self.banco.conexao.commit()
        self.banco.desconectar()

    def deletar_fornecimento(self, cod_produto, cod_fornecedor):
        self.banco.conectar()
        self.banco.cursor.execute(f""" DELETE fornecimento WHERE cod_produto = '{cod_produto}' and cod_fornecedor = '{cod_fornecedor}' """)
        self.banco.conexao.commit()
        self.banco.desconectar()