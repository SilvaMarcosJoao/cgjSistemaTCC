from modulos.dbsqlite import BancoDados
from modulos.fornecedor import Fornecedor
from modulos.produto import  Produto



class Fornecimento:
    # Construtor
    banco = BancoDados()
    fornecedor = Fornecedor()
    prod = Produto()

    def __init__(self, qtd_fornecida=None, data_fornecimento=None) -> None:
        self.__cnpj = []
        self.__cod_produto = []
        self.__qtd_fornecida = qtd_fornecida
        self.__data_fornecimento = data_fornecimento

    # Getters e Setters

    def get_qtd_fornecida(self) -> int:
        return self.__qtd_fornecida

    def set_qtd_fornecida(self, qtd_fornecida: int) -> None:
        self.__qtd_fornecida = qtd_fornecida

    def get_data_fornecimento(self) -> str:
        return self.__data_fornecimento

    def set_data_fornecimento(self, data_fornecimento: str) -> None:
        self.__data_fornecimento = data_fornecimento

    def adicionarProduto(self, produto) -> None:
        self.dadosProd = produto
        self.__cod_produto.append(self.dadosProd[0])
        
    def adicionarFornecedor(self, fornecedor) -> None:
        self.dadosForn = fornecedor
        self.__cnpj.append(self.dadosForn)

    def cadastrar_fornecimento(self, qtd, data) -> None:
        self.codigo = self.adicionarProduto()
        self.cnpj = self.adicionarFornecedor()
        self.banco.conectar()
        self.banco.cursor.execute(f"""INSERT INTO fornecimento (cod_produto, cnpj, qtd_fornecida, data_fornecimento)
                                  VALUES '{self.codigo}', '{self.cnpj}', '{qtd}', '{data}' """)
        self.banco.conexao.commit()
        self.banco.desconectar()