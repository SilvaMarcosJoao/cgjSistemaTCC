

class Cliente:
    def __init__(self,cpf: str, nome_cliente: str, email :str ,telefone: str, logradouro: str, numero : int, cep : int, cidade: str, estado: str ):
        self.__nome_cliente=nome_cliente
        self.__logradouro=logradouro
        self.__cpf=cpf
        self.__telefone=telefone
        self.__email=email
        self.__numero=numero
        self.__cep=cep
        self.__cidade=cidade
        self.__estado=estado

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

    def set_nome_cliente(self, nome_cliente):
        self.__nome_cliente = nome_cliente

    def set_logradouro(self, logradouro):
        self.__logradouro = logradouro

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def set_email(self, email):
        self.__email = email

    def set_numero(self, numero):
        self.__numero = numero

    def set_cep(self, cep):
        self.__cep = cep

    def set_cidade(self, cidade):
        self.__cidade = cidade

    def set_estado(self, estado):
        self.__estado = estado

    def cadastrarCliente(self):
        banco.conectar()
        banco.cursor.execute(f"""Insert into Cliente(cpf, nome_cliente, email,
                          telefone, logradouro, numero, cep, cidade, estado) 
                          values('{self.__cpf }','{self.__nome_cliente }','{self.__email }','{self.__telefone }',
                          '{self.__logradouro }','{self.__numero }','{self.__cep }','{self.__cidade }',
                          '{self.__estado }')""")
        banco.conexao.commit()
        banco.desconectar()
        
    def alterarCliente(self, cod, cpf, nome_cliente, email, telefone, logradouro, numero, cep, cidade, estado):
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
                                WHERE cpf='{cod}'""")
        banco.conexao.commit()
        banco.desconectar()
        
    def listarCliente(self):
        banco.conectar()
        clientes=banco.cursor.execute(f"""SELECT * FROM CLIENTE""").fetchall()   
        print(clientes)   
        banco.desconectar()
        
    def consultarCliente(self, cpf):
        banco.conectar()
        cli = banco.cursor.execute(f"""SELECT cpf, nome_cliente, email,
                          telefone, logradouro, numero, cep, cidade, estado FROM Cliente
                                WHERE cpf='{cpf}'""").fetchmany()
        print(cli)
        banco.desconectar()    
    
    def deletarCliente(self, cpf):
        banco.conectar()
        banco.cursor.execute(f"""DELETE FROM Cliente
                                WHERE cpf='{cpf}'""")
        banco.conexao.commit()
        banco.desconectar()
        
        
cliente2 = Cliente('000.000.000-87', 'Guilherme', 'gsantos809812gasn', '79988888', 'abacate', 12, 34245,'aracaju', 'sergipe')
cliente2.listarCliente()



