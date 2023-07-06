from modulos.dbsqlite import BancoDados
banco = BancoDados()


class OS:
    def __init__(self,cod_os : int=None, cod_cliente: int=None, defeito: str= None, modelo: str= int,
                 data_exec_serv: str= None, valorTotal: float= None, cod_serv: str= None, cod_produto: int= None):
        self.__cod_os=cod_os
        self.__cod_cliente =cod_cliente
        self.__defeito=defeito
        self.__modelo=modelo
        self.__data_exec_serv=data_exec_serv
        self.__valorTotal=valorTotal
        self.__cod_serv = cod_serv
        self.__cod_produto = cod_produto
        
        
    def get_cod_os(self) -> int:
        return self.__cod_os
    
    def get_cod_cliente(self) -> int:
        return self.__cod_cliente 
    
    def get_defeito(self) -> str:
        return self.__defeito
    
    def get_modelo(self) -> str:
        return self.__modelo
    
    def get_data_exec_serv(self) -> str:
        return self.__data_exec_serv
    
    def get_valorTotal(self) -> float:
        return self.__valorTotal
    
    def get_cod_serv(self) -> str:
        return self.__cod_serv
    
    
    def set_cod_os(self, cod_os):
        self.__cod_os=cod_os
        
    def set_cliente(self, cod_cliente):
        self.__cod_cliente = cod_cliente
    
    def set_defeito(self, defeito):
        self.__defeito=defeito
        
    def set_modelo(self, modelo):
        self.__modelo=modelo
    
    def set_data_exec_serv(self, data_exec_serv):
        self.__data_exec_serv=data_exec_serv
        
    def set_valorTotal(self, valorTotal):
        self.__valorTotal=valorTotal
        
    def set_cod_serv(self, cod_serv):
        self.__cod_serv=cod_serv
        
    def set_cod_produto(self, cod_produto):
        self.__cod_produto = cod_produto
    
            
    def RegistrarOS(self):
        banco.conectar()
        banco.cursor.execute(f"""Insert into OS(cod_os, cod_cliente, defeito,
                          modelo, data_exec_serv, valorTotal, cod_serv, cod_produto) 
                          values('{self.__cod_os }','{self.__cod_cliente}',
                          '{self.__defeito}','{self.__modelo}',
                          '{self.__data_exec_serv}','{self.__valorTotal}', 
                          '{self.__cod_serv}','{self.__cod_produto}')""")
        banco.conexao.commit()
        banco.desconectar()
        
    def alterarOS(self, cod_os, cliente, defeito,
                          modelo, data_exec_serv, valorTotal):
        banco.conectar()
        banco.cursor.execute(f"""UPDATE OS
                                SET 
                                 defeito = ('{defeito}'), 
                                 cliente = ('{cliente}') ,
                                 modelo = ('{modelo}'),
                                 data_exec_serv = ('{data_exec_serv}'),
                                 valorTotal= ('{valorTotal}'),
                                WHERE cod_os='{cod_os}'""")
        banco.conexao.commit()
        banco.desconectar()
        
    def listarOS(self):
        banco.conectar()
        OS=banco.cursor.execute(f"""SELECT * FROM OS""").fetchall()   
        print(OS)   
        banco.desconectar()
        
    def consultarOS(self, cod_os):
        banco.conectar()
        OS = banco.cursor.execute(f"""SELECT cod_os, cod_cliente, defeito,
                          modelo, data_exec_serv, valorTotal, cod_serv, cod_produto
                           FROM OS WHERE cod_os='{cod_os}'""").fetchmany()
        print(OS)
        banco.desconectar()    
    
    def deletarOS(self, cod_os):
        banco.conectar()
        banco.cursor.execute(f"""DELETE FROM OS
                                WHERE cod_os='{cod_os}'""")
        banco.conexao.commit()
        banco.desconectar()
        
        #emitirOS