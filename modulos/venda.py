

class Venda:

    def __int__(self, cod_venda: int, cliente: Cliente, valor_total: float, data_venda: str):
        self.__cod_venda = cod_venda
        self.__cliente = cliente
        self.__valor_total = valor_total
        self.__data_venda = data_venda


    def get_cod_venda(self) -> int:
        return self.__cod_venda
    
    def set_cod_venda(self, cod_venda: int) -> None:
        self.__cod_venda = cod_venda

    def get_cliente_venda(self) -> Cliente:
        return self.__cliente
    
    def set_cliente_venda(self, cliente: Cliente) -> None:
        self.__cliente = cliente

    def get_data_venda(self) -> str:
        self.__data_venda
    
    def set_data_venda(self,data: str) -> None:
        self.__data_venda = data 


    def listarVendas(self) -> list:
        db.conectar()
        lista_venda = db.cursor.execute(f""" SELECT * FROM VENDA """).fetchall()
        return lista_venda
    
    def consultarVenda(self):
        pass

    def excluirVenda(self):
        pass

    def emitirVenda(self):
        pass