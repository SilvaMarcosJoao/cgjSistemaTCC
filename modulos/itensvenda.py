
class ItensVenda:
    # CONSTRUTOR
    def __init__(self, cod_produto = None, qtd = None, cod_venda = None) -> None:
        # ATRIBUTOS
        self.__cod_produto = []
        self.__qtd = qtd
        self.__cod_venda = cod_venda

    # GETTERS E SETTERS
    def get_qtd(self) -> int:
        return self.__qtd
    
    def set_qtd(self, qtdItem) -> None:
        self.__qtd = qtdItem

    def get_cod_venda(self) -> int:
        return self.__cod_venda

    def set_cod_venda(self, cod_venda) -> None:
        self.__cod_venda = cod_venda
    