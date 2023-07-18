from modulos.dbsqlite import BancoDados


class ItensVenda:
    banco = BancoDados()
    # CONSTRUTOR
    def __init__(self, cod_produto = None, qtd = None, cod_venda = None, valor = None) -> None:
        # ATRIBUTOS
        self.__cod_produto = cod_produto
        self.__qtd = qtd
        self.__cod_venda = cod_venda
        self.__valor = valor
        self.itens = []

    # GETTERS E SETTERS
    def get_cod_produto(self) -> int:
        return self.__cod_produto
    
    def set_cod_produto(self, cod_prod:int) -> None:
        self.__cod_produto = cod_prod

    def get_qtd(self) -> int:
        return self.__qtd
    
    def set_qtd(self, qtdItem) -> None:
        self.__qtd = qtdItem

    def get_cod_venda(self) -> int:
        return self.__cod_venda

    def set_cod_venda(self, cod_venda:int) -> None:
        self.__cod_venda = cod_venda
    
    def get_valor(self) -> float:
        return self.__valor
    
    def set_valor(self, valorcompra:float) -> None:
        self.__valor = valorcompra

    # MÉTODOS DE CRUD DA CLASSE ITENS VENDA
    def cadastrarItens(self, cod_venda:int, cod_produto:int, qtd:int, valorCompra:float) -> None:
        self.banco.conectar()
        self.banco.cursor.execute(f""" INSERT INTO itens_venda (cod_venda, cod_produto, qtd, valor)
                                    VALUES('{cod_venda}', '{cod_produto}', '{qtd}', '{valorCompra}' ) """)
        self.banco.conexao.commit()
        self.banco.desconectar()

    
