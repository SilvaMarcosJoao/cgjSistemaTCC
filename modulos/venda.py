from modulos.dbsqlite import BancoDados
from modulos.cliente import Cliente
from modulos.produto import Produto

class Venda:
    banco = BancoDados()    
    # CONSTRUTOR
    def __int__(self, cod_venda:int=None, cod_cliente:int=None, valor_total:float=None, data_venda:str=None) -> None:
        # ATRIBUTOS
        self.__cod_venda = cod_venda
        self.__cod_cliente = cod_cliente
        self.__valor_total = valor_total
        self.__data_venda = data_venda

    # GETTERS E SETTERS
    def get_cod_venda(self) -> int:
        return self.__cod_venda
    
    def set_cod_venda(self, cod_venda) -> None:
        self.__cod_venda = cod_venda

    def get_cliente_venda(self) -> int:
        return self.__cod_cliente
    
    def set_cliente_venda(self, cod_cliente) -> None:
        self.__cod_cliente = cod_cliente
        
    def get_valor_total(self) -> float:
        return self.__valor_total
    
    def set_valor_total(self, valor_total:float) -> None:
        self.__valor_total = valor_total

    def get_data_venda(self) -> str:
        self.__data_venda
    
    def set_data_venda(self,data: str) -> None:
        self.__data_venda = data 

    # MÉTODOS DE CRUD DA CLASSE VENDA
    def cadastrarVenda(self, cod_cliente:int, valor_total:float, data_venda:str) -> None:
        self.banco.conectar()
        self.banco.cursor.execute(f"""INSERT INTO Venda(cod_cliente,
                             valor_total, data_venda)
                             VALUES ('{cod_cliente}',
                             '{valor_total}','{data_venda}')""")
        self.banco.conexao.commit()
        self.banco.desconectar()
        
    def listarVendas(self) -> list:
        """
        """
        self.banco.conectar()
        self.vendas = self.banco.cursor.execute(f""" SELECT cod_venda,  cliente.nome_cliente,
                                        valor_total, data_venda
                                      FROM Venda, Cliente
                                      WHERE venda.cod_cliente = cliente.cod_cliente""").fetchall()
        self.banco.desconectar()
        return self.vendas
    
    def consultarVenda(self, cod_venda:int) -> None:
        """
        """
        self.banco.conectar()
        self.vend = self.banco.cursor.execute(f"""SELECT cod_venda, cliente.nome_cliente,
                                    cliente.cpf, valor_total, data_venda
                                    FROM cliente, venda
                                    WHERE venda.cod_cliente = cliente.cod_cliente 
                                     and cod_venda like '{cod_venda}'""").fetchmany()
        self.banco.desconectar()
        return self.vend
    
    def resCodVenda(self):
        self.banco.conectar()
        self.cods = self.banco.cursor.execute(f"""SELECT cod_venda FROM venda 
                                            WHERE cod_venda = (SELECT MAX(cod_venda) FROM venda)  """).fetchall()
        return self.cods
        