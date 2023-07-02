from modulos.dbsqlite import BancoDados
from modulos.fornecedor import Fornecedor
from modulos.produto import  Produto



class Fornecimento:
    # Construtor
    banco = BancoDados()
    fornecedor = Fornecedor()
    prod = Produto()

    def __init__(self, cnpj=fornecedor.get_cpnj_cpf(), cod_produto = prod.get_cod_produto(),  qtd_fornecida=None, data_fornecimento=None) -> None:
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

    def cadastrar_fornecimento(self, cnpj_cpf, cod_produto,data_fornecimento, qtd_fornecida) -> None:
        pass

    def alterar_fornecimento(self) -> None:
        pass
    
    def excluir_fornecimento(self) -> None:
        pass

    def listarFornecedores(self) -> list:
        self.banco.conectar()
        lista = self.banco.cursor.execute(f"""SELECT * FROM fornecimento """).fetchall()
        return lista
