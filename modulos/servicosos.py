from modulos.produto import Produto
from modulos.servico import Servico
from modulos.dbsqlite import BancoDados


banco = BancoDados()

class ServicosOS:
    def __init__(self, cod_serv_os: int, cod_os: int, servico: list ):
        self.__cod_serv_os=cod_serv_os
        self.__cod_os=cod_os
        self.__servico = []
        
    def get_cod_serv_os(self) -> int:
        return self.__cod_serv_os
    
    def get_cod_os(self) -> int:
        return self.__cod_os
    
    def get_Servico(self) -> list:
        return self.__servico
    
    def set_cod_serv_os(self, cod_serv_os):
        self.__cod_serv_os = cod_serv_os
        
    def set_cod_os(self, cod_os):
        self.__cod_os = cod_os
        
    def set_servico(self, servico):
        self.__servico= []
        
    
    def adicionarServicoOs(self, servico):
        banco.conectar()
        servico = []
        Serv=banco.cursor.execute(f"""INSERT INTO ServicosOS(servico), cod_os
                                 values =('{servico : []}'), ('{cod_os}')""")
        banco.commit()
        banco.desconectar()
        
        
    def removerServicoOs(self, servico, cod_serv_os):
        banco.conectar()
        Serv=banco.cursor.execute(f"""Update ServicosOS 
                                 SET servico = {servico}
                                 WHERE cod_serv_os = {cod_serv_os}""")
        
   #necessidade? def finalizarServicoOs():

