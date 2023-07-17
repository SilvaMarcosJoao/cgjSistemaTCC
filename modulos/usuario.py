from modulos.dbsqlite import BancoDados


class Usuario:
    banco = BancoDados()
    #CONSTRUTOR
    def __init__(self):
        # ATRIBUTOS
        self.__cod_usuario = None
        self.__usuario = None
        self.__nome = None
        self.__senha = None

    # GETTERS E SETTERS
    def get_cod_usuario(self) -> int:
        return self.__cod_usuario
    
    def get_usuario(self) -> str:
        return self.__usuario
    
    def get_nome(self) -> str:
        return self.__nome
    
    def get_senha(self) -> str:
        return self.__senha
    
    def set_cod_usuario(self, cod_usuario:int) -> None:
        self.__cod_usuario = cod_usuario
        
    def set_usuario(self, usuario:str) -> None:
        self.__usuario = usuario
        
    def set_nome(self, nome:str) -> None:
        self.__nome = nome
    
    def set_senha(self, senha:str) -> None:
        self.__senha = senha

    # MÉTODOS DE CRUD DA CLASSE USUÁRIO
    def logar(self) -> list:
        """
        Exibe  o usuário e senha. 
        :param: Não tem parâmetro.
        :return: Não tem retorno.
        """
        self.banco.conectar()
        self.res = self.banco.cursor.execute(f""" SELECT usuario, senha FROM usuario""").fetchall()
        return self.res
    
    def alterar_senha(self, senha:str) -> None:
        """
        Altera a senha do usuário do sistema.
        :param: senha, digitada pelo usuário.
        :return: não há retorno.
        """
        self.banco.conectar()
        self.banco.cursor.execute(f""" UPDATE usuario SET senha= '{senha}' WHERE cod_usuario = 1 """)
        self.banco.conexao.commit()