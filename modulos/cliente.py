from modulos.dbsqlite import BancoDados
banco = BancoDados()

class Cliente:
    def __init__(self, cod_cliente: int=None, cpf: str=None, nome_cliente: str=None, email: str=None ,telefone: str=None, logradouro: str=None, numero : int=None, cep : int=None, cidade: str=None, estado: str=None):
        self._cod_cliente=cod_cliente
        self.__nome_cliente=nome_cliente
        self.__logradouro=logradouro
        self.__cpf=cpf
        self.__telefone=telefone
        self.__email=email
        self.__numero=numero
        self.__cep=cep
        self.__cidade=cidade
        self.__estado=estado

    # Getters e Setters
    def get_cod_cliente(self) -> int:
        return self.__cod_cliente
    
    def get_nome_cliente(self) -> str:
        return self.__nome_cliente

    def get_logradouro(self) -> str:
        return self.__logradouro

    def get_cpf(self) -> str:
        return self.__cpf

    def get_telefone(self) -> str:
        return self.__telefone

    def get_email(self) -> str:
        return self.__email

    def get_numero(self) -> int:
        return self.__numero

    def get_cep(self) -> int:
        return self.__cep

    def get_cidade(self) -> str:
        return self.__cidade

    def get_estado(self) -> str:
        return self.__estado
    
    def set_cod_cliente(self, cod:int )-> None:
        self.__cod_cliente = cod

    def set_nome_cliente(self, nome_cliente:str) -> None:
        self.__nome_cliente = nome_cliente

    def set_logradouro(self, logradouro:str) -> None:
        self.__logradouro = logradouro

    def set_cpf(self, cpf: str) -> None:
        self.__cpf = cpf

    def set_telefone(self, telefone:str) -> None:
        self.__telefone = telefone

    def set_email(self, email:str) -> None:
        self.__email = email

    def set_numero(self, numero:int) -> None:
        self.__numero = numero

    def set_cep(self, cep:int) -> None:
        self.__cep = cep

    def set_cidade(self, cidade:str) -> None:
        self.__cidade = cidade

    def set_estado(self, estado:str) -> None:
        self.__estado = estado


    def cadastrarCliente(self, cpf:str, nome_cliente:str, email:str, telefone:str, logradouro:str, numero:int, cep:int, cidade:str, estado:str) -> None:
        banco.conectar()
        banco.cursor.execute(f"""Insert into Cliente(cpf, nome_cliente, email,
                          telefone, logradouro, numero, cep, cidade, estado) 
                          values('{cpf }','{nome_cliente }','{email }','{telefone }',
                          '{logradouro }','{numero }','{cep }','{cidade }',
                          '{estado }')""")
        banco.conexao.commit()
        banco.desconectar()
        
    def alterarCliente(self, cod_cliente:int, cpf:str, nome_cliente:str, email:str, telefone:str, logradouro:str, numero:int, cep:int, cidade:str, estado:str) -> None:
        banco.conectar()
        banco.cursor.execute(f"""UPDATE Cliente
                                SET cpf = ('{cpf }'), 
                                nome_cliente = ('{nome_cliente }') ,
                                email = ('{email }'),
                                telefone = ('{telefone }'),
                                logradouro = ('{logradouro }'),
                                numero = ('{numero }'),
                                cep = ('{cep }'), 
                                cidade= ('{cidade }'), 
                                estado = ('{estado }')
                                WHERE cod_cliente='{cod_cliente}'""")
        banco.conexao.commit()
        banco.desconectar()
        
    def listarCliente(self) -> list :
        banco.conectar()
        clientes=banco.cursor.execute(f"""SELECT * FROM CLIENTE""").fetchall()   
        banco.desconectar()
        return clientes 
    
    def consultarCliente(self, nome:str) -> list:
        banco.conectar()
        cli = banco.cursor.execute(f"""SELECT cod_cliente, cpf, nome_cliente, email,
                          telefone, logradouro, numero, cep, cidade, estado FROM Cliente
                         WHERE nome_cliente like '{nome[0]}%' """).fetchall()              
        banco.desconectar()    
        return cli
    
    def deletarCliente(self, cod_cliente:int) -> None:
        banco.conectar()
        banco.cursor.execute(f"""DELETE FROM Cliente
                                WHERE cod_cliente='{cod_cliente}'""")
        banco.conexao.commit()
        banco.desconectar()

    
    #MÉTODOS PERSONALIZADOS para telaCliente

    def listaperCliente(self) -> list:
        banco.conectar()
        cliente=banco.cursor.execute(f"""SELECT cod_cliente, cpf, nome_cliente FROM CLIENTE""").fetchall()   
        banco.desconectar()
        return cliente
    
    def consultaperCliente(self, nome:str) -> list:
        banco.conectar()
        clis = banco.cursor.execute(f"""SELECT cod_cliente, cpf, nome_cliente FROM Cliente
                         WHERE nome_cliente like '{nome[0]}%' """).fetchall()
        banco.desconectar()    
        return clis
    