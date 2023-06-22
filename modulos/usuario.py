from modulos.dbsqlite import BancoDados

bancoDado = BancoDados()

class Usuario:
    def __init__(self):
        self.__cod_usuario= None
        self.__usuario= None
        self.__nome= None
        self.__senha= None
    
    def get_cod_usuario(self) -> int:
        return self.__cod_usuario
    
    def get_usuario(self) -> str:
        return self.__usuario
    
    def get_nome(self) -> str:
        return self.__nome
    
    def get_senha(self) -> str:
        return self.__senha
    
    def set_cod_usuario(self, cod_usuario: int):
        self.__cod_usuario=cod_usuario
        
    def set_usuario(self, usuario):
        self.__usuario=usuario
        
    def set_nome(self, nome: str):
        self.__nome=nome
    
    def set_senha(self, senha: str):
        self.__senha=senha

    def logar(self) -> None:
        bancoDado.conectar()
        res = bancoDado.cursor.execute(f""" SELECT * FROM usuario""").fetchall()
        print(res)

    def alterar_senha(self, confirma: str):
            bancoDado.conectar()
            bancoDado.cursor.execute(f""" UPDATE usuario SET senha= '{confirma}' WHERE cod_usuario = 1 """)
            bancoDado.conexao.commit()
      
    def sair(self):
        pass

