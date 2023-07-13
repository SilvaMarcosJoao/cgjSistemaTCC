from typing import List
from modulos.dbsqlite import BancoDados
from modulos.cliente import Cliente
from modulos.produto import Produto
banco = BancoDados()

class Venda:

    def __int__(self, cod_venda: int=None, cod_cliente: int=None, cod_produto: int=None , valor_total: float=None, data_venda: str=None):
        self.__cod_venda = cod_venda
        self.__cod_cliente = cod_cliente
        self.__cod_produto = cod_produto
        self.__valor_total = valor_total
        self.__data_venda = data_venda


    def get_cod_venda(self) -> int:
        return self.__cod_venda
    
    def set_cod_venda(self, cod_venda):
        self.__cod_venda = cod_venda

    def get_cliente_venda(self) -> int:
        return self.__cod_cliente
    
    def set_cliente_venda(self, cod_cliente):
        self.__cod_cliente = cod_cliente
        
    def get_cod_produto(self) -> int:
        return self.__cod_produto
    
    def set_cod_produto(self, cod_produto):
        self.__cod_produto = cod_produto
        
    def get_valor_total(self) -> float:
        return self.__valor_total
    
    def set_valor_total(self, valor_total):
        self.__valor_total = valor_total

    def get_data_venda(self) -> str:
        self.__data_venda
    
    def set_data_venda(self,data: str) -> None:
        self.__data_venda = data 


    def cadastrarVenda(self, cod_cliente, cod_produto, valor_total, data_venda ):
        banco.conectar()
        banco.cursor.execute(f"""INSERT INTO Venda(cod_cliente, cod_produto,
                             valor_total, data_venda)
                             VALUES ('{cod_cliente}', '{cod_produto}',
                             '{valor_total}','{data_venda}')""")
        banco.conexao.commit()
        banco.desconectar()
        
    def listarVendas(self) -> list:
        banco.conectar()
        vendas = banco.cursor.execute(f""" SELECT cod_venda, cliente.cod_cliente, cliente.nome_cliente,
                                        valor_total, data_venda
                                      FROM Venda, Cliente ,Produto
                                      WHERE venda.cod_cliente = cliente.cod_cliente""").fetchall()
        banco.desconectar()
        return vendas
    
    def alterarVenda(self, cod_venda,cod_produto, cod_cliente, valor_total, data_venda):
        banco.conectar()
        banco.cursor.execute(f""" UPDATE Venda 
                             SET cod_cliente =('{cod_cliente}'),
                             cod_produto = ('{cod_produto}'),
                             valor_total= ('{valor_total}'),
                             data_venda= ('{data_venda}')
                             WHERE  cod_venda=('{cod_venda}')""")
    
    def consultarVenda(self, cod_venda):
        banco.conectar()
        vend = banco.cursor.execute(f"""SELECT cod_venda, cliente.nome_cliente,
                                    cliente.cpf, desc_produto,
                                    modelo_produto, valor_total, data_venda
                                    FROM cliente, produto, venda
                                    WHERE venda.cod_cliente = cliente.cod_cliente 
                                      AND venda.cod_produto = produto.cod_produto and cod_venda like '{cod_venda}'""").fetchmany()
        banco.desconectar()
        return vend
        
        
    def listarData(self) -> List:
        banco.conectar()
        venD = banco.cursor.execute("""SELECT * FROM Venda WHERE data_venda like '{data_venda}' """).fetchmany()
        banco.desconectar()
        return venD