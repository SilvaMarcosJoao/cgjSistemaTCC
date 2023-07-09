from modulos.dbsqlite import BancoDados

banco = BancoDados()



class Fornecedor:
    # Construtor
    def __init__(self,cod_fornecedor: int=None, cpnj_cpf:str=None, nome_fornecedor:str=None, 
                 email:str=None, telefone:str=None, logradouro:str=None, numero:int=None, cep:int=None,
                 cidade:str=None, estado:str=None) -> None:
        
        # Atributos (privado)
        self.__cod_fornecedor = cod_fornecedor
        self.__cnpj_cpf = cpnj_cpf
        self.__nome_fornecedor = nome_fornecedor
        self.__email = email
        self.__telefone = telefone
        self.__logradouro = logradouro
        self.__numero = numero
        self.__cep = cep
        self.__cidade = cidade
        self.__estado = estado
       # self.__qtd_forn = qtd_forn

    # Getters e Setters
    
    def get_cod_fornecedor(self) -> int:
        return self.__cod_fornecedor

    def set_cod_fornecedor(self, cod_fornecedor:int) -> None:
        self.__cod_fornecedor = cod_fornecedor
    
    def get_cpnj_cpf(self) -> str:
        return self.__cnpj_cpf

    def set_cnpj_cpf(self, cnpj_cpf:str) -> None:
        self.__cnpj_cpf = cnpj_cpf

    def get_nome_fornecedor(self) -> str:
        return self.__nome_fornecedor

    def set_nome_fornecedor(self, nome_fornecedor:str) -> None:
        self.__nome_fornecedor = nome_fornecedor

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email:str) -> None:
        self.__email = email

    def get_telefone(self) -> str:
        return self.__telefone

    def set_telefone(self, telefone:str) -> None:
        self.__telefone = telefone

    def get_logradouro(self) -> str:
        return self.__logradouro

    def set_logradouro(self, logradouro:str) -> None:
        self.__logradouro = logradouro

    def get_numero(self) -> int:
        return self.__numero

    def set_numero(self, numero:int) -> None:
        self.__numero = numero

    def get_cep(self) -> int:
        return self.__cep

    def set_cep(self, cep:int) -> None:
        self.__cep = cep

    def get_cidade(self) -> str:
        return self.__cidade

    def set_cidade(self, cidade:str) -> None:
        self.__cidade = cidade

    def get_estado(self) -> str:
        return self.__estado

    def set_estado(self, estado: str) -> None:
        self.__estado = estado

    def cadastrarFornecedor(self, cnpj, nome_fornecedor, email, telefone, logradouro, numero, cep, cidade, estado) -> None:
        banco.conectar()
        banco.cursor.execute(f""" INSERT INTO fornecedor (cnpj_cpf, 
                                 nome_fornecedor, email, telefone, logradouro, 
                                 numero, cep, cidade, estado)
                                 VALUES ('{cnpj}', '{nome_fornecedor}', '{email}', '{telefone}', '{logradouro}', '{numero}', '{cep}', 
                                 '{cidade}', '{estado}')""")
        banco.conexao.commit()
        banco.desconectar()

    def listarFornecedor(self) -> list:
        banco.conectar()
        fornecedores=banco.cursor.execute(f"""SELECT * FROM FORNECEDOR""").fetchall()   
        banco.desconectar()
        return fornecedores

    def consultarFornecedor(self, nome_fornecedor: str) -> list:
        banco.conectar()
        forn = banco.cursor.execute(f"""SELECT cnpj_cpf, nome_fornecedor,
                                    email, telefone, logradouro, numero, 
                                    cep, cidade, estado FROM fornecedor 
                                    WHERE nome_fornecedor like '{nome_fornecedor[0]}%' """).fetchall()
        banco.desconectar()
        return forn

    def alterarFornecedor(self,cod_fornecedor, cnpj, nome_fornecedor, email, telefone, logradouro, numero, cep, cidade, estado) -> None:
        banco.conectar()
        banco.cursor.execute(f"""UPDATE fornecedor 
        SET cnpj_cpf = '{cnpj}',
        nome_fornecedor = '{nome_fornecedor}',
        email = '{email}',
        telefone = '{telefone}',
        logradouro = '{logradouro}',
        numero = '{numero}',
        cep = '{cep}',
        cidade = '{cidade}',
        estado = '{estado}'
        WHERE cod_fornecedor = '{cod_fornecedor}' """)
        banco.conexao.commit()
        banco.desconectar()

    def excluirFornecedor(self, cod_fornecedor):
        banco.conectar()
        banco.cursor.execute(f"""DELETE FROM fornecedor 
                                 WHERE cod_fornecedor = {cod_fornecedor}""")
        banco.conexao.commit()
        banco.desconectar()
