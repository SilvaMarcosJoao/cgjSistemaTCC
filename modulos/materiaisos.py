#teremos o cod dos serviços 
#e teremos os produtos passando nele 
#from Produtos import produtos 
from modulos.dbsqlite import BancoDados
from modulos.produto import Produto

banco = BancoDados()

class Materiais:
    def __init__(self, produtos: list, cod_serv_os: int):
     self.__produtos= []
     self.__cod_serv_os=cod_serv_os
     
    def get_produtos(self) -> list:
        return self.__produtos
    
    def get_cod_serv_os(self) -> int:
        return self.__cod_serv_os
    
    def set_produtos(self, produtos: list):
        self.__produtos = produtos
        
    def set_cod_serv_os(self, cod_serv_os):
        self.__cod_serv_os = cod_serv_os
 
 #aqui precisa ser passado o material com o codserv, para associar a uma OS
 #
 #      
    def listarMateriaisServ(self):
        banco.conectar()
        Mos=banco.cursor.execute(f"""SELECT * FROM MATERIAIS""").fetchall()   
        print(Mos)   
        banco.desconectar()
        
    def adicionarMateriaisServ(self, produtos):
        banco.conectar()
        Mos=banco.cursor.execute(f"""INSERT INTO MATERIAIS(produtos)
                                 values =('{produtos : []}')""")
        banco.commit()
        banco.desconectar()
        
    def removerMateriaisServ(Self, cod_serv_os,produtos):
        banco.conectar()
        Mos=banco.cursor.execute(f"""Update MATERIAIS 
                                 SET produtos = {produtos}
                                 WHERE cod_serv_os = {cod_serv_os}""")
        banco.commit()
        banco.desconectar()
        
        
